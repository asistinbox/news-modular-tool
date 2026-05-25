import urllib.request
import xml.etree.ElementTree as ET

def fetch_financial_news():
    """
    Module 1: Scraping Module (Updated with User-Agent)
    Fetches the latest financial news headlines and URLs from CNBC.
    """
    url = "https://www.cnbc.com/id/100003114/device/rss/rss.html"
    
    # We add a 'User-Agent' header to make our script look like a standard web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # Create the request with our custom headers
        req = urllib.request.Request(url, headers=headers)
        
        # Open the URL and read the data
        response = urllib.request.urlopen(req)
        data = response.read()
        
        # Parse the XML data
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

# Test execution
if __name__ == "__main__":
    print("Testing Scraping Module with User-Agent...")
    news = fetch_financial_news()
    print(f"Total articles found: {len(news)}")
    for index, article in enumerate(news, 1):
        print(f"\nArticle {index}:")
        print(f"Heading: {article['title']}")
        print(f"URL: {article['url']}")
