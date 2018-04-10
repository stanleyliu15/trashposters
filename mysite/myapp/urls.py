from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

    # Welcome page
    url(r'^$', views.index, name='index'),

    # about-us/
    path('about-us', views.about_us, name='about'),

    # about-us/<team_member>
    path('about-us/<team_member>', views.about_us_single, name="about_us_single"),

    # /profile/<number>
    url(r'profile/(?P<user_id>[A-Za-z0-9]+)/$', views.profile_detail, name='profile_detail'),

    # /posts/
    url(r'^posts/$', views.post_list, name='post_list'),

    # /posts/<number>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

    # /posts/<number>/add_comment
    url(r'posts/(?P<post_id>[0-9]+)/add_comment$', views.create_comment, name='post_comment'),

    # /posts/add/
    url(r'posts/add/$', views.create_post, name='post-add'),

    # /posts/<number>/<comment_id>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.create_comment, name='comment-add'),

    # /register
    url(r'^register/$', views.register, name='register'),

    # /login
    url(r'^login/$', views.login_user, name='login'),

    # /logout
    url(r'logout/$', views.logout_user, name='logout'),

    # path('search/keyword=<keyword>', views.search, name='search'),
    url(r'search/keyword=(?P<keyword>[\w|\W]+)/$', views.search_by_keyword, name='search'),

    # Empty search
    url(r'^search/$', views.search_empty, name='search_empty'),
]
