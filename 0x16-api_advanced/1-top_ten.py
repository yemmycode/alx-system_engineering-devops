#!/usr/bin/python3
"""Defines the top_ten function"""
import requests

def top_ten(subreddit):
    """Display the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    if response.status_code == 404:
        print("None")
        return
    
    # Check if the response contains valid JSON
    try:
        results = response.json().get("data")
    except ValueError:
        print("None")
        return
    
    # Extract and print the titles of the 10 hottest posts
    if results:
        for c in results.get("children", []):
            print(c.get("data", {}).get("title"))
    else:
        print("None")
