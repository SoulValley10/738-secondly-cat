import json
import os
import time
import urllib.request

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

# Interval in seconds (120 = 2 minutes; change to 738 later)
INTERVAL_SECONDS = 738

# Run for 5 hours (18,000 seconds) so it finishes before GitHub's 6-hour limit
MAX_RUNTIME_SECONDS = 5 * 60 * 60
start_time = time.time()


def send_cat():
    req = urllib.request.Request(CAT_API_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as response:
        data = json.loads(response.read().decode())
        cat_image_url = data[0]["url"]

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
    with urllib.request.urlopen(webhook_req, timeout=15) as res:
        print(f"Posted cat! Status: {res.status}")


while (time.time() - start_time) < MAX_RUNTIME_SECONDS:
    try:
        send_cat()
    except Exception as e:
        print(f"Error (retrying next cycle): {e}")

    time.sleep(INTERVAL_SECONDS)
