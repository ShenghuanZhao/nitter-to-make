import os
import requests
import feedparser

print("===== RSS VERSION START =====")

RSS_URL = "https://nitter.net/whyyoutouzhele/rss"

print("Loading RSS...")
print(RSS_URL)

feed = feedparser.parse(RSS_URL)

print("Feed status:", getattr(feed, "status", "unknown"))
print("Entries found:", len(feed.entries))

if len(feed.entries) == 0:
    raise Exception("No tweets found in RSS feed")

tweet = feed.entries[0]

print("Latest title:")
print(tweet.title)

print("Latest link:")
print(tweet.link)

payload = {
    "author": "whyyoutouzhele",
    "title": tweet.title,
    "link": tweet.link
}

print("Sending to MAKE...")

response = requests.post(
    os.environ["MAKE_WEBHOOK"],
    json=payload,
    timeout=30
)

print("MAKE status:", response.status_code)
print("MAKE response:")
print(response.text)

print("===== RSS VERSION END =====")
