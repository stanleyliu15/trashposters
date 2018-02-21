from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about', views.about, name='about'),

	path('about/alex', views.aboutAlex, name='aboutAlex'),
	path('about/danielle', views.aboutDanielle, name='aboutDanielle'),
	path('about/james', views.aboutJames, name='aboutJames'),
	path('about/jzhong', views.aboutJzhong, name='aboutJzhong'),
	path('about/stanley', views.aboutStanley, name='aboutStanley'),
	path('about/tumar', views.aboutTumar, name='aboutTumar'),
]
