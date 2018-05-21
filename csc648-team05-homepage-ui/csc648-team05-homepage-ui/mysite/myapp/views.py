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

        image = "/images/"+str(post.post_id)+"/1.jpg"

    except Posts.DoesNotExist:
        raise Http404(four_oh_four_message)
    comment_list = Comments.objects.filter(post_id=post_id)
    context = {'post': post,
		'image': image,
               'comment_list': comment_list}
    return render(request, 'myapp/post_detail.html', context)



def search(request, keyword):
    print("Keyword: "+keyword)
    #sql_statement = "SELECT * FROM myapp_posts WHERE description LIKE '%%%s%%'"
    #print("sql: "+sql_statement)
    #all_posts = Posts.objects.raw(sql_statement, [keyword])
    all_posts = Posts.objects.filter(description__contains=keyword)

    #iterates through posts to get the images
    images = []
    for x in range(0, len(all_posts)):
        images.append("./images/"+all_posts[x].post_id+"/1.jpg")

    context = {'all_posts': all_posts,
               'images': images,
		       'keyword': keyword}
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


def index(request):
	return render(request, 'views/home/index.html')

def about_us(request):
	with open(os.getcwd() + '/myapp/static/data/about_us_list.json', 'r') as json_file:
  		data = json.load(json_file)
	return render(request, 'views/about/index.html', context={"team_members": data})

def about_us_single(request, team_member):
	with open(os.getcwd() + '/myapp/static/data/about_us_list.json', 'r') as json_file:
  		data = json.load(json_file)[team_member];
	return render(request, 'views/about/about_single.html', context={"team_member": data})

def login(request):
    return render(request, 'views/loginRegister/login.html', context={})

def register(request):
    return render(request, 'views/loginRegister/register.html', context={})
def forgotpassword(request):
    return render(request, 'views/loginRegister/forgotpassword.html', context={})

def contact(request):
    return render(request, 'views/contact/index.html', context={})

def terms_of_service(request):
    return render(request, 'views/terms_of_service.html', context={})

def settings(request):
    return render(request, 'views/settings/index.html', context={})

def create_post(request):
    return render(request, 'views/post/create_post.html', context={})

# for testing the ui
def city_official_dashboard(request):
    return render(request, 'views/dashboard/city_official_dashboard.html', context={})

def city_official_dashboard_view_users(request):
    return render(request, 'views/dashboard/city_official_dashboard_view_users.html', context={})


# for testing the ui
def post_detail_ui(request):
    return render(request, 'views/post/post_detail.html', context={})
