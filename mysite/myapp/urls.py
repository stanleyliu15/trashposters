from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

    # Welcome page
    url(r'^$', views.index, name='index'),

    # about-us/
    path('about-us', views.about_us, name='about_us'),

    # contact/
    path('contact', views.about_us, name='contact'),

    # terms_of_service/
    path('terms-of-service', views.about_us, name='terms_of_service'),

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
    url(r'posts/add/$', views.create_post, name='create_post'),

    # /posts/<number>/<comment_id>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.create_comment, name='comment-add'),

    # /register
    url(r'^register/$', views.register, name='register'),

    # /dashboard
    url(r'^dashboard/$', views.register, name='dashboard_city_official'),

    # /settings
    url(r'^settings/$', views.register, name='settings'),

    # /login
    url(r'^login/$', views.login_user, name='login'),

    # /logout
    url(r'logout/$', views.logout_user, name='logout'),

    # path('search/keyword=<keyword>', views.search, name='search'),
    url(r'search/keyword=(?P<keyword>[\w|\W]+)/$', views.search_by_keyword, name='search'),

    # Empty search
    url(r'^search/$', views.search, name='search_empty'),

    url('search/', views.search, name='get_search'),
]
