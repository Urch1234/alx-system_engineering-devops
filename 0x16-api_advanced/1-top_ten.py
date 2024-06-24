#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        posts = results.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title', "None"))

    except (requests.RequestException, ValueError, KeyError):
        print("None")
