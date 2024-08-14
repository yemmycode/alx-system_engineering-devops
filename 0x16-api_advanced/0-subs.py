#!/usr/bin/python3
"""
Retrieve the number of subscribers for a specific subreddit.
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the total number of subscribers
    for the specified subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=headers)
    
    try:
        return response.json().get('data', {}).get('subscribers', 0)
    except:
        return 0
