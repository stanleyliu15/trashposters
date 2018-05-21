from django.urls import path, re_path
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # for testing the ui
    path('post-detail-ui', views.post_detail_ui, name='post-detail-ui'),

    # city official dashboard
    path('city-official/dashboard', views.city_official_dashboard, name='city_official_dashboard'),
    path('city-official/dashboard/users', views.city_official_dashboard_view_users, name='city_official_dashboard'),

    # contact
    path('contact', views.contact, name='contact'),

    # about us
    path('about-us', views.about_us, name='about_us'),
    path('about-us/<team_member>', views.about_us_single, name="about_us_single"),

    # login&register
    path('login', views.login, name='login'),
    path('register', views.register, name="register"),
    path('forgotpassword', views.forgotpassword, name="forgotpassword"),


    # create post
    path('create-post', views.create_post, name='create_post'),

    # settings
    path('settings', views.settings, name='settings'),

    # terms of service
    path('terms-of-service', views.terms_of_service, name='terms_of_service'),

    # /posts/
    url(r'^posts/$', views.post_list, name='post_list'),

    # /posts/<number>
    url(r'posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

    # Empty search
    url(r'^search/$', views.search, name='search_empty'),

    # Searches by different aspects of a post
    url(r'^search/title=(?P<title>[A-Za-z0-9]+)/$', views.search_by_title, name='search_title'),
    url(r'^search/description=(?P<description>[A-Za-z0-9]+)/$', views.search_by_description, name='search_description'),
    url(r'^search/hazard_type=(?P<hazard_type>[A-Za-z0-9]+)/$', views.search_by_hazard_type, name='search_hazard_type'),
    url(r'^search/location=(?P<location>[A-Za-z0-9]+)/$', views.search_by_location, name='search_location'),
    url(r'^search/user=(?P<username>[A-Za-z0-9]+)/$', views.search_by_user, name='search_user'),
]
