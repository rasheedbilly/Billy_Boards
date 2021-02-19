from django.shortcuts import render
import requests
import json
from . import models

# Create your views here.
def home(request):
	context = {
		'title': 'Landing Page',
	}
	return render(request, 'Board_App/home.html', context)

def about(request):
	context = {
		'title': 'About Page',
	}
	return render(request, 'Board_App/about.html', context)