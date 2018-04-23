from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse

from .models import Posts
from .models import Comments
from .models import UserData
from .models import PostImageCollection

from .forms import UserForm
from .forms import LoginForm
from .forms import PostForm
from .forms import CommentForm
from .forms import SearchForm
from .forms import ImageForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from geopy.geocoders import Nominatim

import os, json

four_oh_four_message = "This page cannot be found."


def index(request):
    """
    Loads the welcome page for the website.
    :param request:
    :return: The index.html page.
    """
    return render(request, 'index.html', context={})


def create_post(request):
    """
    Creates a new post and writes it to the database if the request is HTTP Get.
    If the user is not logged it, will redirect the user to the login page.
    @:param     An http request.
    @:return    Renders a new page with the post detail information and the primary key as part of the url.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        image_form = ImageForm(request.POST, request.FILES)
    else:
        form = PostForm()
        image_form = ImageForm()
    if request.user.is_authenticated:
        if form.is_valid() and image_form.is_valid():
            post = form.save(commit=False)
            this_username = request.user
            user = User.objects.get(username=this_username)
            post.user_id = user
            post.save()
            # Once post has been written to the database,
            # we can use the primary key to create the foreign
            # key in the images table and save that form.
            images = image_form.save(commit=False)
            images.post_id = post
            images.save()
            context = {'post': post,
                       'images': images}
            return redirect('post_detail', post_id=post.post_id)
    else:
        return render(request, 'myapp/login.html')
    context = {
        "form": form,
        "image_form": image_form
    }
    return render(request, 'views/post/create_post.html', context)


def create_comment(request, post):
    """
    Creates a new comment writes it to the database if the comment form is valid.
    @:param     An http request.
    @:return    Renders the post_detail page on the current post id with the new comment
    """
    form = CommentForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            comment = form.save(commit=False)
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
    address = post.location
    geolocation = Nominatim()
    location = geolocation.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    image_collection = PostImageCollection.objects.get(post_id=post_id)
    post_images = [image_collection.image1, image_collection.image2, image_collection.image3, image_collection.image4]
    context = {'post': post,
               'image': image,
               'comment_list': comment_list,
               'form': form,
               'latitude': latitude,
               'longitude': longitude,
               'post_images': post_images
              }
    return render(request, 'views/post/post_detail.html', context)


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


def search(request):
    form = SearchForm(request.GET)
    context = {'form': form}
    if request.method == 'GET':
        if form.is_valid():
            selection = request.GET.get('filter-post-menu')
            value = request.GET.get('query')
            if selection == 'title':
                all_posts = Posts.objects.filter(title__icontains=value)
                context['all_posts'] = all_posts
            if selection == 'zipcode':
                all_posts = Posts.objects.filter(zipcode__icontains=value)
                context['all_posts'] = all_posts
        else:
             all_posts = Posts.objects.all()
             context['all_posts'] = all_posts
    return render(request, 'search.html', context)


def search_empty(request):
    """
    Handles an empty search bar.
    @:param     An http request.
    @:return    Renders a page with all posts listed.
    """
    all_posts = Posts.objects.all()
    form = SearchForm(request.GET)
    context = {'all_posts': all_posts,
               'form': form,
               'keyword': ''}
    return render(request, 'search.html', context)


def search_by_title(request, title):
    """
    Searches the title of posts to find matching posts containing the title keyword.
    @:param     An http request with a title keyword.
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(title__icontains=title)
    context = {'all_posts': all_posts,
               'keyword': title}
    return render(request, 'search.html', context)


def search_by_description(request, description):
    """
    Searches the description of posts to find matching posts containing the keyword.
    @:param     An http request with a keyword.
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(description__icontains=description)
    context = {'all_posts': all_posts,
               'keyword': description}
    return render(request, 'search.html', context)


def search_by_user(request, username):
    """
    Searches the description of posts to find matching posts made by the requested user
    @:param     An http request with a username
    @:return    Renders a page with all matching posts listed.
    """
    #all_posts = Posts.objects.filter(user_id__username__exact=username)
    all_posts = Posts.objects.filter(user_id__username__icontains=username)
    context = {'all_posts': all_posts,
               'keyword': username}
    return render(request, 'search.html', context)


def search_by_hazard_type(request, hazard_type):
    """
    Searches the description of posts to find matching posts of the given hazard Type
    @:param     An http request with a hazard type
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(hazard_type__hazard_name__exact=hazard_type)
    context = {'all_posts': all_posts,
               'keyword': hazard_type}
    return render(request, 'search.html', context)


def search_by_location(request, location):
    """
    Searches the description of posts to find locations containing the given query
    @:param     An http request with a hazard type
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(location__icontains=location)
    context = {'all_posts': all_posts,
               'keyword': location}
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


def about_us(request):
    """
    Loads the index page for the about-us section of the website.
    :param request:
    :return: The about-us page rendered as html.
    """
    with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
        data = json.load(json_file)
    return render(request, 'about-pages/index.html', context={"team_members": data})


def about_us_single(request, team_member):
    """
    Returns an individual about page for a team member.
    :param request:     An HTML request
    :param team_member: The team member the user would like to see information about
    :return:            An HTML page rendered with that team member's information.
    """
    with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
        data = json.load(json_file)[team_member];
    return render(request, 'about-pages/about-single.html', context={"team_member": data})
