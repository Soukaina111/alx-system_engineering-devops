#!/usr/bin/python3
"""
Fetches and returns a list of titles for all hot posts from a
specified subreddit using the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit. If no results are found, returns None.
    """
    httpp = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_params = '?show="all"&limit=100&after={}'.format(after)
    url = httpp + endpoint + query_params
    headers = {'User-Agent': 'ALXSE/1.0'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        return None
    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
        after = data['after']
        if after:
            recurse(subreddit, hot_list, after)
    return hot_list
