import requests
from sendEmail import send_email
import os

API = os.environ.get('API_KEY')
TOPIC = "tesla"
print(API)

URL = "https://newsapi.org/v2/everything?" \
       f"q={TOPIC}&" \
      "sortBy=publishedAt&" \
      f"apiKey={API}&" \
      "language=en"

print(URL)

# Make request
request = requests.get(URL, timeout=10)

# Get a dictionary with data
content = request.json()
print(content)
BODY = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        BODY = "Subject: Today's NEWS" + "\n" + BODY + article["title"] + "\n" \
            + article["description"] + "\n"  \
            + article["url"] + 2*"\n"

BODY = BODY.encode("utf-8")

send_email(message=BODY)
