from django.shortcuts import render
from .models import Posts
from django.http import HttpResponse


# Called when user goes to post/<number>
def post_list(request):
    all_posts = Posts.objects.all()
    html = "<h2> Posts so far </h2>"
    for post in all_posts:
        url = '/post/' + str(post.post_id) + '/'
        html += '<a href=' + url + '> ' + post.title + '</a><br>'
    return HttpResponse(html)


def post_detail(request, post_id):
    post = Posts.objects.get()
    html = '<h2> Details for: ' + str(post_id) + '</h2>'
    return HttpResponse(html)

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})


def index2(request):
    return render(request, 'index2.html', context={})


def about(request):
    return render(request, 'about.html', context={})


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
