import urllib.request
import json

print("Testing Scraping Module with Currents API...")

# Replace with your free token
API_KEY = "773e934a6c194faa9428542af6a0cda6"
url = f"https://api.currentsapi.services/v1/latest-news?language=en&limit=5&apiKey={API_KEY}"

try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            print(f"\nSuccessfully fetched {len(data['news'])} articles!\n")
            for article in data['news']:
                print(f"- {article['title']}")
                print(f"  Source: {article['author']} | URL: {article['url']}\n")
        else:
            print(f"Unexpected status code: {response.status}")
except Exception as e:
    print(f"Error fetching news: {e}")
