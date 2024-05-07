#!/usr/bin/python3
"""
Fetches and displays the titles of the top 10 hot posts from a
specified subreddit using the Reddit API
"""
import requests


def top_ten(subreddit):
    """ Define the base URL for the Reddit API to do the job"""
    base_url = "https://www.reddit.com/r/"
    endpoint = "hot.json"
    url = base_url + subreddit + endpoint
    headers = {
        "User-Agent": "ALXSE/0.0.1"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        hot_posts = data.get('data', {}).get('children', [])
    if hot_posts:
        for post in hot_posts[:10]:
            print(post['data']['title'])
    else:
        print("No hot posts found.")
    else:
        print(None)
