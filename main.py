import requests

API_KEY = ""
URL = "https://newsapi.org/v2/everything?q=tesla" \
    "&from=2023-09-07&sortBy=publishedAt&apiKey=" \
    "71ffe15533b34c179171d17e61c66fce"

# Make request
request = requests.get(URL, timeout=10)

# Get a dictionary with data
content = request.json()


for article in content["articles"]:
    print(article["title"])
