from bs4 import BeautifulSoup
import requests
import re
from bs4 import MarkupResemblesLocatorWarning
import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

url_to_scrape = "https://books.toscrape.com/"

def getHTMLdocument(url):
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


html_document = getHTMLdocument(url_to_scrape)
soup = BeautifulSoup(html_document, 'html.parser')


links = [link for link in soup.find_all('a')]
sub_urls = [url_to_scrape + link.get('href') for link in links if link.get('href') and "catalogue/category/books/" in link.get('href')]
#len_of_prefix_url = len(sub_urls[0]) # 52nd index

for sub_url in sub_urls:
    print(sub_url)

def getPageRequest(urls: list[str]):
    webpages = {} # Store HTML Parsed Info. Webpage : HTML Parse.
    webpage_to_book = {} # Webpage : List of Books.
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            print("Response Success.")
            # Parse HTML
            webpages[url] = BeautifulSoup(response.text, 'html.parser')

        if response.status_code == 404:
            print("Response Failed.")

    return webpages



# Select a few sub-URLs to test
test_urls = sub_urls[:3]  # First 3 category pages

# Call your function
parsed_pages = getPageRequest(test_urls)

# Print the title of each parsed page to verify
for url, soup in parsed_pages.items():
    print(f"\nTitle for {url}:")
    print(soup.title.text.strip())
