from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html', context={})

def index2(request):
	return render(request, 'index2.html', context={})

def about(request):
	return render(request, 'about.html', context={})

def aboutAlex(request):
	return render(request, 'about-pages/alex.html', context={})

def aboutDanielle(request):
	return render(request, 'about-pages/danielle.html', context={})

def aboutJames(request):
	return render(request, 'about-pages/james.html', context={})

def aboutJzhong(request):
	return render(request, 'about-pages/jzhong.html', context={})

def aboutStanley(request):
	return render(request, 'about-pages/stanley.html', context={})

def aboutTumar(request):
	return render(request, 'about-pages/tumar.html', context={})