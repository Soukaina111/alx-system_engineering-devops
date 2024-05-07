#!/usr/bin/python3
"""
Fetches and displays the titles of the top 10 hot posts from a
specified subreddit using the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches and displays the titles of the top 10 hot posts from a
    specified subreddit using the Reddit API
    """
    # base_url = "https://www.reddit.com/r/"
    # Define the endpoint for subreddit information
    # endpoint = "about.json"
    # Construct the full URL
    # url = base_url + subreddit + endpoint
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'ALXESE/0.0.0'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscribers1 = response.json().get('data').get('subscribers')
    return subscribers1
