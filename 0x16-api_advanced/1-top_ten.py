#!/usr/bin/python3
"""Top Ten Module"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    If the subreddit is not valid, prints "None".
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            if data:
                for child in data:
                    print(child.get("data", {}).get("title"))
            else:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")
