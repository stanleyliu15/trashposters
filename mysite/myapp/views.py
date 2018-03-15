from django.shortcuts import render
from django.template import loader

from .models import Posts
from django.http import HttpResponse


# Lists all of the posts
def post_list(request):
    all_posts = Posts.objects.all()
    template = loader.get_template('myapp/post_list.html')
    context = {'all_posts': all_posts}
    return HttpResponse(template.render(context, request))


# Lists details about the post when the user clicks on it.
def post_detail(request, post_id):
    post = Posts.objects.get(pk=post_id)
    url = '/posts/'
    html = '<h2> Details for: ' + str(post.title) + '</h2>'
    html += '<br> ' \
            'Posted by:  ' + str(post.user_id) + '<br><br>' \
            'Description: ' + post.description + '<br>' \
            + 'Location: ' + post.location\
            + '<br> <a href=' + url + '> Go back </a>'
    return HttpResponse(html)

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
