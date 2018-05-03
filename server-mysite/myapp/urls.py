from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [

    # Welcome page
    path('', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
    

    # for testing the ui
    path('post-detail-ui', views.post_detail_ui, name='post-detail-ui'),
    path('city-official/dashboard', views.city_official_dashboard, name='city_official_dashboard'),
    path('city-official/dashboard/view_posts', views.city_official_dashboard_view_posts, name='dashboard_city_official_view_posts'),
    path('city-official/dashboard/view_users', views.city_official_dashboard_view_users, name='dashboard_city_official_view_users'),

    # about-us/
    path('about-us', views.about_us, name='about_us'),
    path('about-us/<team_member>', views.about_us_single, name="about_us_single"),

    # contact/
    path('contact', views.contact, name='contact'),

    # terms_of_service/
    path('terms-of-service', views.terms_of_service, name='terms_of_service'),
    

    # /profile/<number>
    url(r'profile/(?P<user_id>[A-Za-z0-9]+)/$', views.profile_detail, name='profile_detail'),


    # /create-post/
    path('create-post', views.create_post, name='create_post'),

    # /posts/
    url(r'^posts/$', views.post_list, name='post_list'),

    # /posts/<number>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

    # /posts/<number>/add_comment
    url(r'posts/(?P<post_id>[0-9]+)/add_comment$', views.create_comment, name='post_comment'),

    # /posts/add/
    url(r'posts/add/$', views.create_post, name='create_post'),

    # /posts/<number>/<comment_id>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.create_comment, name='comment-add'),

    # /dashboard
    url(r'^dashboard/$', views.register, name='dashboard_city_official'),

    # /login and /register
    url(r'^login/$', views.login_user, name='login'),
    url(r'^register/$', views.register, name='register'),


    # /logout
    url(r'logout/$', views.logout_user, name='logout'),

    path('settings', views.settings, name='settings'),

    # Empty search
    url(r'^search/$', views.search, name='search_empty'),


    # Searches by different aspects of a post
    #url(r'^search/title=(?P<title>[A-Za-z0-9]+)/$', views.search_by_title, name='search_title'),
    url(r'^search/(?P<select>[A-Za-z]+)=(?P<query>[A-Za-z0-9]+)/$', views.search_by, name='search'),
    #url(r'^search/description=(?P<description>[A-Za-z0-9]+)/$', views.search_by_description, name='search_description'),
    #url(r'^search/hazard_type=(?P<hazard_type>[A-Za-z0-9]+)/$', views.search_by_hazard_type, name='search_hazard_type'),
    #url(r'^search/location=(?P<location>[A-Za-z0-9]+)/$', views.search_by_location, name='search_location'),
    #url(r'^search/user=(?P<username>[A-Za-z0-9]+)/$', views.search_by_user, name='search_user'),

]
