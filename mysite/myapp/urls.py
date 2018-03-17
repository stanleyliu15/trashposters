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

    url(r'search/keyword=(?P<keyword>[a-zA-Z0-9]+)/$', views.search, name='search'),
]
