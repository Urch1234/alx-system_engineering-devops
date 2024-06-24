#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if invalid.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent)
    
    if response.status_code != 200:
        return 0
    
    try:
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except (ValueError, AttributeError):
        return 0
