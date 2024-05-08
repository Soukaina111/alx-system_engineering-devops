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
    base_url = "https://www.reddit.com/r/"
    # Define the endpoint for subreddit information
    endpoint = "info.json"
    # Construct the full URL
    url = base_url + subreddit + endpoint
    headers = {'User-Agent': 'ALXESE/0.0.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None
    else:
        subscribers = response.json().get('data').get('subscribers')
        if subscribers is None:
            print("Subreddit does not exist or is private.")
            return None
        return subscribers
