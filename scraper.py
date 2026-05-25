import urllib.request
import xml.etree.ElementTree as ET

def fetch_financial_news():
    """
    Module 1: Scraping Module
    Fetches the latest financial news headlines and URLs from CNBC.
    """
    url = "https://www.cnbc.com/id/100003114/device/rss/rss.html"
    
    try:
        # Open the URL and read the data
        response = urllib.request.urlopen(url)
        data = response.read()
        
        # Parse the XML data
        root = ET.fromstring(data)
        items = root.findall('.//item')
        
        articles = []
        for item in items[:5]: # Let's just grab the top 5 articles for now
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

# This part lets us test the module
if __name__ == "__main__":
    print("Testing Scraping Module...")
    news = fetch_financial_news()
    for index, article in enumerate(news, 1):
        print(f"\nArticle {index}:")
        print(f"Heading: {article['title']}")
        print(f"URL: {article['url']}")
