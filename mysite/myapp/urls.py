from django.urls import path, re_path
from django.conf.urls import url


from . import views

urlpatterns = [
    # TODO: Replace the about pages with a regular expression so it's like the posts urls.
    path('', views.index, name='index'),

    # about us
    path('about-us', views.aboutUs, name='aboutUs'),
    path('about-us/<team_member>', views.aboutUsSingle, name="aboutUsSingle"),

    # /posts/
    url(r'^posts/$', views.post_list, name='post_list'),

    # /posts/<number>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

    #path('search/keyword=<keyword>', views.search, name='search'),
    url(r'search/keyword=(?P<keyword>[\w|\W]+)/$', views.search, name='search'),
    url('search', views.search_empty, name='search2'),
]
