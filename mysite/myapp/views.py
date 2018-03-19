from django.shortcuts import render
from django.http import Http404

from .models import Posts
from .models import Comments

from pprint import pprint
import os
import json

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
    comment_list = Comments.objects.filter(post_id=post_id)
    context = {'post': post,
               'comment_list': comment_list}
    return render(request, 'myapp/post_detail.html', context)

def search_empty(request):
    print("Search empty")
    all_posts = Posts.objects.all()
    context={
    'all_posts': all_posts,
    'keyword': ''
    }
    return render(request, 'search.html', context)

def search(request, keyword):
    print("Keyword: "+keyword)
    #sql_statement = "SELECT * FROM myapp_posts WHERE description LIKE '%%%s%%'"
    #print("sql: "+sql_statement)
    #all_posts = Posts.objects.raw(sql_statement, [keyword])
    all_posts = Posts.objects.filter(description__contains=keyword)
    context = {'all_posts': all_posts,
		'keyword': keyword}
    return render(request, 'search.html', context)

# Create your views here.
# Going to replace all of these with a regular expression to reduce the amount of methods in views.py - Danielle
def index(request):
		return render(request, 'views/home/index.html')

def aboutUs(request):
		with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
  			data = json.load(json_file)
		return render(request, 'views/about-us/index.html', context={"team_members": data})

def aboutUsSingle(request, team_member):
		with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
  			data = json.load(json_file)[team_member];
		return render(request, 'views/about-us/about-single.html', context={"team_member": data})
