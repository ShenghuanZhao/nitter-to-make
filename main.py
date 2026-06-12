import os
import feedparser
import requests

RSS_URL = "https://nitter.net/whyyoutouzhele/rss"

feed = feedparser.parse(RSS_URL)

print("entries:", len(feed.entries))

if not feed.entries:
    raise Exception("No tweets found")

tweet = feed.entries[0]

payload = {
    "author": "whyyoutouzhele",
    "title": tweet.title,
    "link": tweet.link,
    "published": getattr(tweet, "published", "")
}

response = requests.post(
    os.environ["MAKE_WEBHOOK"],
    json=payload,
    timeout=30
)

print("status:", response.status_code)
