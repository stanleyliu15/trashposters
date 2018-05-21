from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse

from .models import Posts
from .models import Comments
from .models import UserData
from .models import PostImageCollection


from .forms import *

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
    posts = Posts.objects.all()
    # sorts by date and gets the most recent 5
    recent_posts = posts.order_by('-date')[:10]
    context = {'recent_posts': recent_posts}
    return render(request, 'new_regular/index.html', context)


def check_city_official(user):
    """
    :param user from request.user
    :return: True if they're a city official, false otherwise.
    """
    if user.groups.filter(name="CityOfficial").exists():
        return True
    else:
        return False


def create_post(request):
    """
    Creates a new post and writes it to the database if the request is HTTP Get.
    If the user is not logged it, will redirect the user to the login page.
    @:param     An http request.
    @:return    Renders a new page with the post detail information and the primary key as part of the url.
    """
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        image_form = ImageForm(request.POST, request.FILES)
    else:
        post_form = PostForm()
        image_form = ImageForm()
    if request.user.is_authenticated:
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            this_username = request.user
            user = User.objects.get(username=this_username)
            post.user_id = user
            # If the user is a city official, mark the post as so.
            if check_city_official(user):
                post.city_official = True
            else:
                post.city_official = False
            # Assign foreign key to the post.
            hazard_type = post_form.cleaned_data['hazard_type']
            hazard_type_foreign_key = HazardType.objects.get(hazard_name=hazard_type)
            post.hazard_type = hazard_type_foreign_key
            # save latitude and longitude
            address = post.location
            geolocation = Nominatim()
            location = geolocation.geocode(address)
            post.latitude = location.latitude
            post.longitude = location.longitude
            post.save()
            # Once post has been written to the database,
            # we can use the primary key to create the foreign
            # key in the images table and save that form.
            images = image_form.save(commit=False)
            images.post_id = post
            images.save()
            post.preview_image = images.image1
            post.save()
            context = {'post': post,
                       'images': images}
            return redirect('/posts/'+str(post.post_id))
    else:
        return render(request, 'new_regular/login.html')
    context = {
        "post_form": post_form,
        "image_form": image_form
    }
    return render(request, 'new_regular/create_post.html', context)


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
            return render(request, 'new_regular/post_detail.html', context)
    else:
        return render(request, 'new_regular/login.html')
    context = {
        "form": form,
    }
    return render(request, 'new_regular/post_detail.html', context)


def post_list(request):
    """
    Retrieves all of the Post objects from the database and lists them.
    @:param     An http request.
    @:return    Renders a page with all of the posts listed.
    """
    all_posts = Posts.objects.all()
    all_posts.reverse()
    context = {'all_posts': all_posts}
    return render(request, 'new_regular/post_list.html', context)


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
    post_images = list()
    image_1 = image_collection.image1
    image_2 = image_collection.image2
    image_3 = image_collection.image3
    image_4 = image_collection.image4
    if image_1 is not None:
        post_images.append(image_1)
    if image_2 is not None:
        post_images.append(image_2)
    if image_3 is not None:
        post_images.append(image_3)
    if image_4 is not None:
        post_images.append(image_4)

    context = {'post': post,
               'image': image,
               'comment_list': comment_list,
               'form': form,
               'latitude': latitude,
               'longitude': longitude,
               'image_1': image_1,
               'image_2': image_2,
               'image_3': image_3,
               'image_4': image_4,
               'post_images': post_images
              }
    return render(request, 'new_regular/post_detail.html', context)


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
    return render(request, 'new_regular/profile_detail.html', context)


def search_empty(request):
    """
    Handles an empty search bar.
    @:param     An http request.
    @:return    Renders a page with all posts listed.
    """
    all_posts = Posts.objects.all()
    context = {'posts': all_posts,
               'extra_posts': all_posts,
               'select': "",
               'keyword': ""}
    return render(request, 'new_regular/search.html', context)


def search_by(request, select, query):
    """
    Searches difference aspects of a post depending on what the user selects
    @:param     An http request with a title keyword.
    @:return    Renders a page with all matching posts listed.
    """

    context = {'posts': Posts.objects.none(),
               'extra_posts': None,
               'select': select,
               'keyword': query}
 
    if select=="all" or select=="title":
        context['posts'] = context['posts'] | Posts.objects.filter(title__icontains=query)
    if select=="all" or select=="description":
        context['posts'] = context['posts'] |  Posts.objects.filter(description__icontains=query)
    if select=="all" or select=="user":
        context['posts'] = context['posts'] |  Posts.objects.filter(user_id__username__exact=query)
    if select=="all" or select=="hazard_type":
        context['posts'] = context['posts'] |  Posts.objects.filter(hazard_type__hazard_name__exact=query)
    if select=="all" or select=="location":
        context['posts'] = context['posts'] |  Posts.objects.filter(location__icontains=query)

    # gets all posts if no results
    if len(context['posts']) == 0:
        context['extra_posts'] = Posts.objects.all()

    return render(request, 'new_regular/search.html', context)



def register(request):
    """
    Registers a user to the website if a valid form is given and filled in.
    This registration adds a user to django.contrib.auth.models.User.
    @:param     An http request.
    @:return    A login success page with the user now logged in to the website.
    """
    template_name = 'new_regular/register.html'
    user_signup_form = UserSignUpForm(request.POST or None)
    user_data_form = UserDataForm(request.POST or None)
    if user_signup_form.is_valid() and user_data_form.is_valid():
        # Creates new user through django's authentication system.
        user = user_signup_form.save(commit=False)
        username = user_signup_form.cleaned_data['username']
        password = user_signup_form.cleaned_data['password']
        user.set_password(password)
        user.save()
        # Validates user data, links it to a foreign key, and saves it.
        user_data = user_data_form.save(commit=False)
        user_data.username = user
        user_data.save()
        # Logs the user in.
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(index)
    context = {
        "user_signup_form": user_signup_form,
        "user_data_form": user_data_form
    }

    return render(request, template_name, context)


def login_user(request):
    """
    Logs the user in if valid credentials are given. Utilizes django.contrib.auth.authenticate in order
    to validate username and password.
    @:param     An http request
    @:return    A login success page with the user now logged in to the website.
    """
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(index)
                else:
                    return render(request, 'new_regular/login.html', {'error_message': 'You have been banned.'})
            else:
                return render(request, 'new_regular/login.html', {'form': form, 'error_message': 'Invalid login'})
    context = {
         "form": form,
    }
    return render(request, 'new_regular/login.html', context)


def logout_user(request):
    """
    Logs the user out if they are logged in. Utilizes django.contrib.auth.logout
    @:param     An http request
    @:return    The index page of the website.
    """
    logout(request)
    return redirect(index)


def forgotpassword(request):
    return render(request, 'new_regular/forgotpassword.html', context={})


def about_us(request):
    """
    Loads the index page for the about-us section of the website.
    :param request:
    :return: The about-us page rendered as html.
    """
    with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
        data = json.load(json_file)
    return render(request, 'new_regular/about.html', context={"team_members": data})


def about_us_single(request, team_member):
    """
    Returns an individual about page for a team member.
    :param request:     An HTML request
    :param team_member: The team member the user would like to see information about
    :return:            An HTML page rendered with that team member's information.
    """
    with open(os.getcwd() + '/myapp/static/data/about-us-list.json', 'r') as json_file:
        data = json.load(json_file)[team_member];
    return render(request, 'new_regular/about_single.html', context={"team_member": data})


def contact(request):
    return render(request, 'new_regular/contact.html', context={})


def terms_of_service(request):
    return render(request, 'new_regular/terms_of_service.html', context={})


def settings(request):
    return render(request, 'new_regular/settings.html', context={})


# for testing the ui
def city_official_dashboard(request):
    """
    City official users only.
    :param request:
    :return:
    """
    user = request.user
    if check_city_official(user):
        if request.POST:
            pass
        userdata = UserData.objects.get(username=user)
        city = userdata.city
        posts = Posts.objects.filter(location__icontains=city)
        constituents = UserData.objects.filter(city__icontains=city)
        context = {
            "city": city,
            "constituents": constituents
        }
        if posts is not None:
            context['posts'] = posts
        else:
            context['error_message'] = "No posts found for your city."
        return render(request, 'new_regular/city_official.html', context)
    else:
        return redirect(index)


def city_official_dashboard_view_posts(request):
    return render(request, 'new_regular/city_official_dashboard_view_posts.html', context={})


def city_official_dashboard_view_users(request):
    return render(request, 'new_regular/city_official_dashboard_view_users.html', context={})


# for testing the ui
def post_detail_ui(request):
    return render(request, 'new_regular/post_detail.html', context={})
