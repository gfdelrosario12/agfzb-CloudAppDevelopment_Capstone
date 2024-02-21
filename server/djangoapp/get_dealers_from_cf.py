def get_dealer_details(request, dealer_id):
    """
    Retrieve details of a dealer including reviews.

    :param request: HTTP request object.
    :param dealer_id: ID of the dealer.
    :return: HTTP response object.
    """
    # Get dealer details
    dealer = get_dealer_by_id_from_cf(dealer_id)
    if dealer is None:
        return HttpResponseNotFound("Dealer not found")

    # Get reviews for the dealer
    reviews = get_dealer_reviews_from_cf(dealer_id)

    # If reviews exist, print sentiment for each review
    if reviews:
        for review in reviews:
            print(f"Review: {review.review}, Sentiment: {review.sentiment}")

    # Render the details template with dealer and reviews
    return render(request, 'dealer_details.html', {'dealer': dealer, 'reviews': reviews})
