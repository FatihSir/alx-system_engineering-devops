#!/usr/bin/python3
"""Top Ten Module"""

import requests


def top_ten(subreddit):
    """
    a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
        else:
            for child in data:
                print(child.get("data", {}).get("title"))

    except requests.RequestException:
        print("None")
