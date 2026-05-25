import urllib.request
import json

print("Testing Scraping Module with NewsAPI.org...")

# TODO: Replace with your actual NewsAPI.org API key
API_KEY = "773e934a6c194faa9428542af6a0cda6"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

# Advanced headers to disguise the GitHub Actions cloud environment
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1'
}

try:
    # Construct the request with the masked headers
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            # Decode and parse the JSON payload
            raw_data = response.read().decode('utf-8')
            data = json.loads(raw_data)
            
            articles = data.get('articles', [])
            print(f"\nSuccessfully fetched {len(articles)} articles!\n")
            
            for article in articles:
                # Fallback to 'Unknown' if source name or author is missing
                source_name = article.get('source', {}).get('name', 'Unknown Source')
                title = article.get('title', 'No Title')
                article_url = article.get('url', '#')
                
                print(f"- {title}")
                print(f"  Source: {source_name} | URL: {article_url}\n")
        else:
            print(f"Unexpected status code: {response.status}")

except urllib.error.HTTPError as e:
    print(f"Error fetching news: {e}")
    if e.code == 403:
        print("\n[Notice]: NewsAPI is still hard-blocking the GitHub Action IP address block.")
        print("If this happens, you will need to fall back to the Mediastack solution.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
