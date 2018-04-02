from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse

from .models import Posts
from .models import Comments
from .models import UserData

from .forms import UserForm
from .forms import LoginForm
from .forms import PostForm
from .forms import CommentForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import os, json

four_oh_four_message = "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! " \
                       "A wittle fucko boingo! The code monkeys at our " \
                       "headquarters are working VEWY HAWD to fix this!"


# WELCOME TO OUR SITE YOU ENVIRONMENT LOVER
def index(request):
    return render(request, 'index.html', context={})


def create_post(request):
    """
    Creates a new post and writes it to the database if the request is HTTP Get.
    If the user is not logged it, will redirect the user to the login page.
    @:param     An http request.
    @:return    Renders a new page with the post detail information and the primary key as part of the url.
    """
    form = PostForm(request.POST, request.FILES or None)
    if request.user.is_authenticated:
        if form.is_valid():
            post = form.save(commit=False)
            this_username = request.user
            user = User.objects.get(username=this_username)
            post.user_id = user
            post.image = form.cleaned_data['image']
            post.save()
            context = {'post': post}
            return render(request, 'myapp/post_detail.html', context)
    else:
        return render(request, 'myapp/login.html')
    context = {
        "form": form,
    }
    return render(request, 'myapp/posts_form.html', context)


def create_comment(request):
    """
    Creates a new comment writes it to the database if the comment form is valid.
    @:param     An http request.
    @:return    Renders the post_detail page on the current post id with the new comment
    """
    form = CommentForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            post = form.save(commit=False)
            this_username = request.user
            user = User.objects.get(username=this_username)
            post.user_id = user
            post.save()
            context = {'post': post}
            return render(request, 'myapp/post_detail.html', context)
    else:
        return render(request, 'myapp/login.html')
    context = {
        "form": form,
    }
    return render(request, 'myapp/post_detail.html', context)


def post_list(request):
    """
    Retrieves all of the Post objects from the database and lists them.
    @:param     An http request.
    @:return    Renders a page with all of the posts listed.
    """
    all_posts = Posts.objects.all()
    all_posts.reverse()
    context = {'all_posts': all_posts}
    return render(request, 'myapp/post_list.html', context)


def post_detail(request, post_id):
    """
    Renders a page with the post details corresponding to the given id. If the
    id does not match any posts within the database, will display a 404 instead.
    @:param     An http request.
    @:return    Renders a page with the post details.
    @:except    Http404 if the post id given does not correspond with any existing posts.
    """
    form = CommentForm(request.POST or None)
    try:
        post = Posts.objects.get(pk=post_id)
        image = "/images/" + str(post.post_id) + "/1.jpg"
    except Posts.DoesNotExist:
        raise Http404(four_oh_four_message)
    comment_list = Comments.objects.filter(post_id=post_id)
    context = {'post': post,
               'image': image,
               'comment_list': comment_list,
               'form': form}
    return render(request, 'myapp/post_detail.html', context)


def profile_detail(request, user_id):
    """
    Renders a page with the post details corresponding to the given id. If the
    id does not match any posts within the database, will display a 404 instead.
    @:param     An http request.
    @:return    Renders a page with the post details.
    @:except    Http404 if the post id given does not correspond with any existing posts.
    """
    try:
        userdata = UserData.objects.get(username__username__exact=user_id)
    except User.DoesNotExist:
        raise Http404(four_oh_four_message)
    context = {'userdata': userdata}
    return render(request, 'myapp/profile_detail.html', context)


def search_empty(request):
    """
    Handles an empty search bar.
    @:param     An http request.
    @:return    Renders a page with all posts listed.
    """
    all_posts = Posts.objects.all()
    context = {'all_posts': all_posts,
               'keyword': ''}
    return render(request, 'search.html', context)


def search_by_keyword(request, keyword):
    """
    Searches the description of posts to find matching posts containing the keyword.
    @:param     An http request with a keyword.
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(description__contains=keyword)
    context = {'all_posts': all_posts,
               'keyword': keyword}
    return render(request, 'search.html', context)


def search_by_user(request, username):
    """
    Searches the description of posts to find matching posts made by the requested user
    @:param     An http request with a username
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(user_id__username__exact=username)
    context = {'all_posts': all_posts,
               'username': username}
    return render(request, 'search.html', context)


def search_by_hazard_type(request, hazard_type):
    """
    Searches the description of posts to find matching posts of the given hazard Type
    @:param     An http request with a hazard type
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(hazard_type__hazard_name__exact=hazard_type)
    context = {'all_posts': all_posts,
               'hazard_type': hazard_type}
    return render(request, 'search.html', context)


def search_by_location(request, location):
    """
    Searches the description of posts to find locations containing the given query
    @:param     An http request with a hazard type
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(location__contains=location)
    context = {'all_posts': all_posts,
               'location': location}
    return render(request, 'search.html', context)


def register(request):
    """
    Registers a user to the website if a valid form is given and filled in.
    This registration adds a user to django.contrib.auth.models.User.
    @:param     An http request.
    @:return    A login success page with the user now logged in to the website.
    """
    template_name = 'register.html'
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # TODO: Create registration successful page with redirect or show user is now logged in.
                return HttpResponse('Login successful.')
    context = {
        "form": form,
    }
    return render(request, template_name, context)


def login_user(request):
    """
    Logs the user in if valid credentials are given. Utilizes django.contrib.auth.authenticate in order
    to validate username and password.
    @:param     An http request
    @:return    A login success page with the user now logged in to the website.
    """
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(index)
            else:
                return render(request, 'login.html', {'error_message': 'You have been banned.'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    context = {
         "form": form,
    }
    return render(request, 'login.html', context)


def logout_user(request):
    """
    Logs the user out if they are logged in. Utilizes django.contrib.auth.logout
    @:param     An http request
    @:return    The index page of the website.
    """
    logout(request)
    return redirect(index)


# About pages index
def about_us(request):
    with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
        data = json.load(json_file)
    return render(request, 'about-pages/index.html', context={"team_members": data})


# About pages individual page for each team member
def about_us_single(request, team_member):
    with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
        data = json.load(json_file)[team_member];
    return render(request, 'about-pages/about-single.html', context={"team_member": data})