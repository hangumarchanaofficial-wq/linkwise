from bs4 import BeautifulSoup
import requests

def scrape_url(url):
   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers , TimeoutError=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        #Remove unwanted tags/content for the websites
        
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'form']):
            element.decompose()
        article = soup.find('article') or soup.find('main') or soup.find('body')
        
        if article:
            # Get text and clean up whitespace
            lines = (line.strip() for line in article.get_text().splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            # Limit text length to avoid overloading Gemma 3 context window
            return text[:8000] 
        
        return "Could not find readable content on this page."

    except Exception as e:
        return f"Error during scraping: {str(e)}"
        
