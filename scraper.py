import urllib.request
import json

print("Testing Scraping Module with Open Developer API...")

try:
    url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=5"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            print(f"\nSuccessfully fetched {len(data['results'])} articles!\n")
            for article in data['results']:
                print(f"- {article['title']}")
                print(f"  Source: {article['news_site']} | URL: {article['url']}\n")
        else:
            print(f"Unexpected status code: {response.status}")

except Exception as e:
    print(f"Error fetching news: {e}")
