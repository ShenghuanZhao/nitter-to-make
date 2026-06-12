import os
import json
import requests
import feedparser

RSS_URL = "https://nitter.net/whyyoutouzhele/rss"

print("===== NITTER CHECK START =====")

feed = feedparser.parse(RSS_URL)

if len(feed.entries) == 0:
    raise Exception("No tweets found")

tweet = feed.entries[0]

current_link = tweet.link
current_title = tweet.title

print("Latest tweet:")
print(current_title)
print(current_link)

# 读取状态文件
with open("state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

last_link = state.get("last_link", "")

print("Previous link:")
print(last_link)

# 去重判断
if current_link == last_link:
    print("No new tweet. Exit.")
    raise SystemExit(0)

print("New tweet detected!")

payload = {
    "title": current_title,
    "link": current_link
}

response = requests.post(
    os.environ["MAKE_WEBHOOK"],
    json=payload,
    timeout=30
)

print("MAKE status:", response.status_code)

# 更新状态文件
state["last_link"] = current_link

with open("state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print("State updated.")
print("===== NITTER CHECK END =====")

