from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Posts
from .models import Comments
from .models import Users

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


# Lists all of the posts
def post_list(request):
    all_posts = Posts.objects.all()
    all_posts.reverse()
    context = {'all_posts': all_posts}
    return render(request, 'myapp/post_list.html', context)


# Lists details about the post when the user clicks on it.
def post_detail(request, post_id):
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
    all_posts = Posts.objects.all()
    context = {'all_posts': all_posts,
               'keyword': ''}
    return render(request, 'search.html', context)


# sql_statement = "SELECT * FROM myapp_posts WHERE description LIKE '%%%s%%'"
# print("sql: "+sql_statement)
# all_posts = Posts.objects.raw(sql_statement, [keyword])
def search(request, keyword):
    print("Keyword: " + keyword)
    all_posts = Posts.objects.filter(description__contains=keyword)
    context = {'all_posts': all_posts,
               'keyword': keyword}
    return render(request, 'search.html', context)


# Adds a user to the admin.auth.users table. Displays an error message if the username is already taken.
def register(request):
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


# INITIALIZE ALL VALUES
# Logs in an existing user by validating their username and password.
def login_user(request):
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


# Logs a user out.
def logout_user(request):
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
