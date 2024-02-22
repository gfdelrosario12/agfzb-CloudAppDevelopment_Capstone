from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        # Creating an empty context dictionary
        context = {}
        
        # Get dealer reviews from the URL
        reviews = get_dealer_reviews_from_cf(dealer_id)
        
        # Add the reviews list to the context
        context['reviews'] = reviews
        
        # Return the dealer_details.html template with the context
        return render(request, 'djangoapp/dealer_details.html', context)

# Your other views...

# Dummy function to avoid NameError
def get_dealer_reviews_from_cf(dealer_id):
    pass

def my_view(request):
    return render(request, 'static_template.html')


def about_page(request):
    return render(request, 'djangoapp/about.html')


def contact_page(request):
    return render(request, 'djangoapp/contact.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')  # Adjust the URL name if necessary
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'djangoapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('djangoapp:home')  # Adjust the URL name if necessary


def registration_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('djangoapp:index')  # Adjust the URL name if necessary
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})


def get_dealerships(request):
    if request.method == "GET":
        # Creating an empty context dictionary
        context = {}
        
        url = "http://127.0.0.1:8000//dealerships/get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf("https://bd477862-4c69-452f-8486-783b6bb3189a-bluemix.cloudantnosqldb.appdomain.cloud")
        
        # Add the dealerships list to the context
        context['dealerships'] = dealerships
        
        # Return the index.html template with the context
        return render(request, 'djangoapp/index.html', context)


# Add your other views here


# Dummy functions to avoid NameError
def get_dealers_from_cf(url):
    pass

def post_request(url, json_payload, dealerId):
    pass
