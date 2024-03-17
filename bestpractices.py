# scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Fetches HTML content from the specified URL and returns it.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4XX/5XX errors
        return response.content      # Returns the content of the response
    except requests.RequestException as e:
        print(f"Error fetching the HTML content: {e}")
        return None

def extract_price(html_content):
    """
    Extracts the price from the provided HTML content using BeautifulSoup.
    Handles different encodings properly to avoid UnicodeEncodeError.
    """
    try:
        # Using 'html.parser' to avoid additional dependencies
        soup = BeautifulSoup(html_content, 'html.parser')
        price_span = soup.find('span', class_='aok-offscreen')
        if price_span:
            price_text = price_span.text.strip()
            return price_text
        else:
            return 'Price not found'
    except Exception as e:
        print(f"Error extracting price: {e}")
        return None

# Usage example
if __name__ == "__main__":
    url = 'https://www.amazon.com/dp/example'  # Replace with the actual product URL
    html_content = fetch_html(url)
    if html_content:
        price = extract_price(html_content)
        print(f"Extracted price: {price}")
