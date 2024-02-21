from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
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
            print("Success")
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid username or password.')
            print("Error")
    # If the request method is GET or authentication fails, render the login page
    return render(request, 'djangoapp/login.html')  # Replace 'login.html' with the path to your login template

# Create a `logout_request` view to handle sign out request
def logout_view(request):
    logout(request)
    # Redirect to a page after logout, for example, the home page
    return redirect('djangoapp:home')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('index.html')  # Assuming 'index' is the URL pattern name for the index page
            print("Success")
    else:
        form = UserCreationForm()
        print("Registration Error")
    return render(request, 'djangoapp/registration.html', {'form': form})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "http://127.0.0.1:8000//dealerships/get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf("https://bd477862-4c69-452f-8486-783b6bb3189a-bluemix.cloudantnosqldb.appdomain.cloud")
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required
def add_review(request, dealer_id):
    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        if review_text:
            url = "http://127.0.0.1:8000/add_review"  # Adjust the URL accordingly
            review = {
                "time": datetime.utcnow().isoformat(),
                "name": request.user.username,
                "dealership": dealer_id,
                "review": review_text,
                "purchase": False  # Adjust this value based on your requirements
            }
            json_payload = {
                "review": review
            }
            response = post_request(url, json_payload, dealerId=dealer_id)
            if response.status_code == 200:
                messages.success(request, 'Review submitted successfully.')
                return redirect('dealer_details', dealer_id=dealer_id)
            else:
                messages.error(request, 'Failed to submit review.')
        else:
            messages.error(request, 'Review text is required.')
    else:
        messages.error(request, 'Invalid request method.')
    # Redirect to a page displaying dealer details or handle as required
    return redirect('dealer_details', dealer_id=dealer_id)