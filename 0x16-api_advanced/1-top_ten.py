#!/usr/bin/python3
"""
Fetches and displays the titles of the top 10 hot posts from a
specified subreddit using the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Fetches and displays the titles of the top 10 hot posts from a
    specified subreddit using the Reddit API
    """
    httpp = "https://www.reddit.com/r/"
    endpoint = "hot.json"
    url = httpp + subreddit + endpoint
    headers = {'User-Agent': "ALXSE/0.0.1"}
    response = requests.get(url, headers=headers)
    try:
        tt = response.json()['data']['children']
        for post in tt:
            print(post['data']['title'])
    except KeyError:
        print("None")
