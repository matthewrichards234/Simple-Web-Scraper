from bs4 import BeautifulSoup
import requests
import re
from bs4 import MarkupResemblesLocatorWarning
import warnings
import time
import random
from currency_converter import CurrencyConverter

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

c = CurrencyConverter()

url_to_scrape = "https://books.toscrape.com/"
response = requests.get(url_to_scrape)
soup = BeautifulSoup(response.text, 'html.parser')

links = [link for link in soup.find_all('a')]
sub_urls = [url_to_scrape + link.get('href') for link in links if link.get('href') and "catalogue/category/books/" in link.get('href')]


def mapWebpageToBooks(webpage_list: dict[str, BeautifulSoup]):
    webpage_to_books = {}  # Webpage : List of books

    for url, soup in webpage_list.items():
        books = {}
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title_tag = article.find("h3").find("a")
            book_title = title_tag.get("title")
            price_tag = article.find("p", class_="price_color")
            price = price_tag.text.strip() if price_tag else "N/A"
            books[book_title] = price

        webpage_to_books[url] = books

        # Convert Pounds to US Dollars
        for book, price in books.items():
            price_match = re.search(r"[\d.]+", price)
            if price_match:
                try:
                    converted_price = float(price_match.group()) # We can now manipulate this float value.
                    pounds_to_dollars = c.convert(converted_price, 'GBP', 'USD')
                    books[book] = round(pounds_to_dollars, 2)
                except Exception as e:
                    books[book] = "Conversion failed"
            else:
                books[book] = "N/A"

    return webpage_to_books


def getPageRequest(urls: list[str]):
    webpages = {}  # Store HTML Parsed Info. Webpage : HTML Parse.
    for url in urls:
        response = requests.get(url)

        # Add a delay before making requests
        delay = random.uniform(1, 3)
        time.sleep(delay)

        if response.status_code == 200:
            response.encoding = 'utf-8'
            print(f"Response Success for {url}.")
            # Parse HTML
            webpages[url] = BeautifulSoup(response.text, 'html.parser')

        if response.status_code == 404:
            print(f"Response Failed for {url}.")

    return webpages



test_urls = sub_urls[:3]  # First 3 category pages

parsed_pages = getPageRequest(test_urls)

webpage_to_books = mapWebpageToBooks(parsed_pages)

for url, books in webpage_to_books.items():
    print(f"\nBooks in category {url}:")
    for book, price in books.items():
        print(f"Book: {book}, Price (USD): {price}")
