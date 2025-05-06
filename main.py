from bs4 import BeautifulSoup
import requests
import re

url_to_scrape = "https://books.toscrape.com/"

def getHTMLdocument(url):
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text

html_document = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

#print(soup.prettify())

for link in soup.find_all('a'): 
    print(link.get('href'))   