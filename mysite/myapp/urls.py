from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: Replace the about pages with a regular expression so it's like the posts urls.
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('about/alex', views.aboutAlex, name='aboutAlex'),
    path('about/danielle', views.aboutDanielle, name='aboutDanielle'),
    path('about/james', views.aboutJames, name='aboutJames'),
    path('about/jzhong', views.aboutJzhong, name='aboutJzhong'),
    path('about/stanley', views.aboutStanley, name='aboutStanley'),
    path('about/tumar', views.aboutTumar, name='aboutTumar'),

    # /posts/
    url(r'^posts/$', views.post_list, name='post_list'),

    # /posts/<number>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

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
    url(r'search/keyword=(?P<keyword>[\w|\W]+)/$', views.search, name='search'),
    url(r'^search/$', views.search_empty, name='search_empty'),
]
