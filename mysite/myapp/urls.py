from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [

    # Site wide ---------------------------------------------------
    # Welcome page
    path('', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
    # for testing the ui
    path('post-detail-ui', views.post_detail_ui, name='post-detail-ui'),
    path('city-official/dashboard', views.city_official_dashboard, name='city_official_dashboard'),
    path('city-official/dashboard/view_posts', views.city_official_dashboard_view_posts, name='dashboard_city_official_view_posts'),
    path('city-official/dashboard/view_users', views.city_official_dashboard_view_users, name='dashboard_city_official_view_users'),
    path('about-us', views.about_us, name='about_us'),
    path('about-us/<team_member>', views.about_us_single, name="about_us_single"),
    path('contact', views.contact, name='contact'),
    path('terms-of-service', views.terms_of_service, name='terms_of_service'),
    

    # Posts ---------------------------------------------------
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

    # User Accounts ---------------------------------------------------
    # /dashboard
    url(r'^dashboard/$', views.register, name='dashboard_city_official'),
    # /profile/<number>
    url(r'profile/(?P<user_id>[A-Za-z0-9]+)/$', views.profile_detail, name='profile_detail'),
    # /login and /register
    url(r'^login/$', views.login_user, name='login'),
    url(r'^register/$', views.register, name='register'),
    # /logout
    url(r'logout/$', views.logout_user, name='logout'),
    path('forgotpassword', views.forgotpassword, name="forgotpassword"),
    path('settings', views.settings, name='settings'),


    # Search ---------------------------------------------------
    # Empty search
    url(r'^search/$', views.search_empty, name='search_empty'),
    url(r'^search/(?P<select>[A-Za-z]+)=(?P<query>.*)/$', views.search_by, name='search'),

]
