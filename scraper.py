import urllib.request
import json

def fetch_financial_news():
    """
    Module 1: Scraping Module (Switched to an Open Developer API)
    Fetches latest news items safely from an open data network without getting blocked.
    """
    # Using a fully open, public developer endpoint that welcomes cloud scripts
    url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=5"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        
        # This API gives us clean JSON data (built-in Python dictionary format)
        data = json.loads(response.read().decode())
        
        articles = []
        # Extract data from the API response format
        for item in data.get('results', []):
            articles.append({
                "title": item.get('title'),
                "url": item.get('url')
            })
            
        return articles

    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

if __name__ == "__main__":
    print("Testing Scraping Module with Open Developer API...")
    news = fetch_financial_news()
    print(f"Total articles found: {len(news)}")
    for index, article in enumerate(news, 1):
        print(f"\nArticle {index}:")
        print(f"Heading: {article['title']}")
        print(f"URL: {article['url']}")
