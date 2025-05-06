from bs4 import BeautifulSoup
import requests
import re
from bs4 import MarkupResemblesLocatorWarning
import warnings
import time
import random

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

url_to_scrape = "https://books.toscrape.com/"

links = [link for link in soup.find_all('a')]
sub_urls = [url_to_scrape + link.get('href') for link in links if link.get('href') and "catalogue/category/books/" in link.get('href')]


def mapWebpageToBooks(webpage_list: dict[str, BeautifulSoup]):
    webpage_to_books = {}  # Webpage : List of books
    for url, soup in webpage_list.items():
        books = []
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title_tag = article.find("h3").find("a")
            book_title = title_tag.get("title")
            books.append(book_title)

        webpage_to_books[url] = books

    return webpage_to_books


def getPageRequest(urls: list[str]):
    webpages = {}  # Store HTML Parsed Info. Webpage : HTML Parse.
    for url in urls:
        response = requests.get(url)

        # Add a delay before making requests
        delay = random.uniform(1, 3)
        time.sleep(delay)

        if response.status_code == 200:
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
    for book in books:
        print(book)
