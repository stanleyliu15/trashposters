from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html', context={})

def index2(request):
	return render(request, 'index2.html', context={})
