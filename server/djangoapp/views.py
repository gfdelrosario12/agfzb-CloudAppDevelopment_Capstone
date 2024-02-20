from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def my_view(request):
    return render(request, 'static_template.html')

# Create an `about` view to render a static about page
def about_page(request):
    return render(request, 'djangoapp/about.html')

# Create a `contact` view to return a static contact page
def contact_page(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('djangoapp/index.html')  # Replace 'home' with the name of your home page URL
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid username or password.')
    # If the request method is GET or authentication fails, render the login page
    return render(request, 'djangoapp/login.html')  # Replace 'login.html' with the path to your login template

# Create a `logout_request` view to handle sign out request
def logout_view(request):
    logout(request)
    # Redirect to a page after logout, for example, the home page
    return redirect('djangoapp/index.html')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('djangoapp/index.html')  # Replace 'home' with the name of your home page URL
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})  # Replace 'signup.html' with the path to your signup template

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
