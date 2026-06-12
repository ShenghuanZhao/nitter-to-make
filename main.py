import os
import requests
import feedparser

RSS_URL = "https://nitter.net/whyyoutouzhele/rss"

feed = feedparser.parse(RSS_URL)

print("entries:", len(feed.entries))

if len(feed.entries) == 0:
    raise Exception("No tweets found")

tweet = feed.entries[0]

payload = {
    "author": "whyyoutouzhele",
    "title": tweet.title,
    "link": tweet.link
}

response = requests.post(
    os.environ["MAKE_WEBHOOK"],
    json=payload,
    timeout=30
)

print("make status:", response.status_code)
