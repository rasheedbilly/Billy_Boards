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

def contact(request):
	context = {
		'title': 'Contact Us!',
	}
	return render(request, 'Board_App/contact.html', context)

def shop(request):
	context = {
		'title': 'Shop Page',
	}
	return render(request, 'Board_App/shop.html', context)