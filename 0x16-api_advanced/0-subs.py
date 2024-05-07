#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns
    the number of total subscribers for a given
    subreddit.
    """
    # Define the base URL for the Reddit API
    base_url = "https://www.reddit.com/r/"
    # Define the endpoint for subreddit information
    endpoint = "info.json"
    # Construct the full URL
    url = base_url + subreddit + endpoint
    headers = {
                "User-Agent": "YourAppName/0.0.1"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:
        return 0
