from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse

from .models import Posts
from .models import Comments

from .forms import UserForm
from .forms import LoginForm
from .forms import PostForm
from .forms import CommentForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

four_oh_four_message = "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! " \
                       "A wittle fucko boingo! The code monkeys at our " \
                       "headquarters are working VEWY HAWD to fix this!"


def create_post(request):
    """
    Creates a new post and writes it to the database if the request is HTTP Get.
    If the user is not logged it, will redirect the user to the login page.
    @:param     An http request.
    @:return    Renders a new page with the post detail information and the primary key as part of the url.
    """
    form = PostForm(request.POST or None)
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


def search(request, keyword):
    """
    Searches the description of posts to find matching posts containing the keyword.
    @:param     An http request with a keyword.
    @:return    Renders a page with all matching posts listed.
    """
    all_posts = Posts.objects.filter(description__contains=keyword)
    context = {'all_posts': all_posts,
               'keyword': keyword}
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


# Create your views here.
def index(request):
    return render(request, 'index.html', context={})


def index2(request):
    return render(request, 'index2.html', context={})


def about(request):
    return render(request, 'about.html', context={})


# TODO Replace all of these with a regular expression to reduce the amount of methods in views.py - Danielle
def aboutAlex(request):
    return render(request, 'about-pages/alex.html', context={})


def aboutDanielle(request):
    return render(request, 'about-pages/danielle.html', context={})


def aboutJames(request):
    return render(request, 'about-pages/james.html', context={})


def aboutJzhong(request):
    return render(request, 'about-pages/jzhong.html', context={})


def aboutStanley(request):
    return render(request, 'about-pages/stanley.html', context={})


def aboutTumar(request):
    return render(request, 'about-pages/tumar.html', context={})
