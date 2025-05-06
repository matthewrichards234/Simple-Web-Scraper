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

links = [link for link in soup.find_all('a')]
sub_urls = []

for link in links:
    href = link.get('href')
    #print(href)

    # add genre to "catalogue/category/books/" !
    # f.E: catalogue/category/books/horror

    if "catalogue/category/books/" in href:
        sub_urls.append(url_to_scrape + "catalogue/category/books/")


for sub_url in sub_urls:
    print(sub_url)
    

split_url = sub_urls[0].split('/') 
print(split_url)
idx_to_replace = split_url[-1]
category_idx = split_url[6]
print(category_idx)