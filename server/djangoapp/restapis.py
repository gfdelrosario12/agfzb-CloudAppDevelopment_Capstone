import requests
from requests.auth import HTTPBasicAuth
from .models import DealerReview
from . import analyze_review_sentiments

def get_dealer_reviews_from_cf(url, dealer_id, api_key):
    """
    Gets reviews by dealer's id from a cloud function and assigns sentiment using Watson NLU.

    :param url: The URL of the cloud function endpoint.
    :param dealer_id: The ID of the dealer.
    :param api_key: The API key for authentication.
    :return: List of DealerReview objects.
    """
    # Make GET request to fetch reviews by dealer's ID
    response = get_request(url, params={'dealerId': dealer_id}, headers={'Content-Type': 'application/json'}, auth=HTTPBasicAuth('apikey', api_key))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        reviews_data = response.json()

        # Convert JSON data into a list of DealerReview objects
        dealer_reviews = []
        for review_data in reviews_data:
            # Create a DealerReview object
            dealer_review = DealerReview(
                dealership_id=review_data['dealership_id'],
                name=review_data['name'],
                purchase=review_data['purchase'],
                review=review_data['review'],
                purchase_date=review_data['purchase_date'],
                car_make=review_data['car_make'],
                car_model=review_data['car_model'],
                car_year=review_data['car_year'],
                sentiment=analyze_review_sentiments(review_data['review']),
                id=review_data['id']
            )
            # Append the DealerReview object to the list
            dealer_reviews.append(dealer_review)

        return dealer_reviews
    else:
        # If request failed, return None
        return None

def post_request(url, json_payload, **kwargs):
    """
    Makes a POST request with JSON payload.

    :param url: The URL to send the POST request to.
    :param json_payload: The JSON payload to send.
    :param kwargs: Additional keyword arguments to pass to the requests.post method.
    :return: The response object.
    """
    response = requests.post(url, json=json_payload, **kwargs)
    return response