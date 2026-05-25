import urllib.request
import xml.etree.ElementTree as ET

def fetch_financial_news():
    """
    Module 1: Scraping Module (Switched to Yahoo Finance)
    Fetches the latest financial news headlines and URLs.
    """
    # Yahoo Finance RSS feed for top financial/market news
    url = "https://finance.yahoo.com/news/rssindex"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read()
        
        root = ET.fromstring(data)
        items = root.findall('.//item')
        
        articles = []
        for item in items[:5]: # Grab top 5 articles
            title = item.find('title').text
            link = item.find('link').text
            
            articles.append({
                "title": title,
                "url": link
            })
            
        return articles

    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

if __name__ == "__main__":
    print("Testing Scraping Module with Yahoo Finance...")
    news = fetch_financial_news()
    print(f"Total articles found: {len(news)}")
    for index, article in enumerate(news, 1):
        print(f"\nArticle {index}:")
        print(f"Heading: {article['title']}")
        print(f"URL: {article['url']}")
