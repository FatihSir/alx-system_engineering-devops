# 0x16. API advanced
![Api](1.jpeg)

The **Reddit API** allows developers to interact with Reddit’s platform programmatically. You can access Reddit’s vast community-driven content, from posts and comments to user profiles and subreddit information. This repository includes scripts that demonstrate how to fetch, process, and manipulate data from Reddit’s API, as well as other APIs, for various use cases such as data analysis, content aggregation, and more.

Whether you’re looking to integrate Reddit data into your application, analyze trends, or simply explore what the Reddit API has to offer, this repository serves as a solid starting point.

## Resources
- [Reddit API Documentaion](https://www.reddit.com/dev/api/)
- [String Query](https://en.wikipedia.org/wiki/Query_string)

## Tasks
#### 0. How many subs?

Write a function that queries the `Reddit API` and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```shell
wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
```
##### Repo:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x16-api_advanced`
- File: `0-subs.py`
