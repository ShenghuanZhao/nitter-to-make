import os
import requests

webhook = os.environ["MAKE_WEBHOOK"]

payload = {
    "source": "github",
    "message": "hello from github actions"
}

response = requests.post(
    webhook,
    json=payload,
    timeout=30
)

print("status:", response.status_code)
print(response.text)
