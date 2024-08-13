#!/usr/bin/python3
"""Module for counting words in subreddit titles."""

import requests


def count_words(subreddit, word_list, counts_dict=None, after=None):
    """
    Recursively queries the Reddit API and counts the occurrences of words
    in word_list within the titles of all hot posts in the specified subreddit.
    """
    if counts_dict is None:
        counts_dict = {word.lower(): 0 for word in word_list}

    headers = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")

    posts = data.get("children")
    for post in posts:
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            counts_dict[word.lower()] += title.count(word.lower())

    after = data.get("after")
    if after is None:
        sorted_counts = sorted(counts_dict.items(),
                               key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
    else:
        return count_words(subreddit, word_list, counts_dict, after)
