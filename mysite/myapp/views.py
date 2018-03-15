from django.shortcuts import render
from django.http import Http404

from .models import Posts

four_oh_four_message = "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! " \
                       "A wittle fucko boingo! The code monkeys at our " \
                       "headquarters are working VEWY HAWD to fix this!"


# Lists all of the posts
def post_list(request):
    all_posts = Posts.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'myapp/post_list.html', context)


# Lists details about the post when the user clicks on it.
def post_detail(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
    except Posts.DoesNotExist:
        raise Http404(four_oh_four_message)
    context = {'post': post}
    return render(request, 'myapp/post_detail.html', context)

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})


def index2(request):
    return render(request, 'index2.html', context={})


def about(request):
    return render(request, 'about.html', context={})

# Going to replace all of these with a regular expression to reduce the amount of methods in views.py - Danielle
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
