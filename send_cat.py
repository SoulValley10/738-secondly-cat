import json
import os
import urllib.request

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

# 1. Fetch a random cat image URL
req = urllib.request.Request(CAT_API_URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    cat_image_url = data[0]["url"]

# 2. Send the image URL to your Discord channel
payload = json.dumps({"content": cat_image_url}).encode("utf-8")
webhook_req = urllib.request.Request(
    WEBHOOK_URL,
    data=payload,
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    },
    method="POST",
)

with urllib.request.urlopen(webhook_req) as res:
    print(f"Posted cat! Status code: {res.status}")
