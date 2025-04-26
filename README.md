# Simple-Web-Scraper

## Goal:
Write a Python script that grabs real data from a website and saves it.

---

## Basic Requirements:
- Use **requests** to fetch a web page.
- Use **BeautifulSoup** to parse the HTML.
- Extract specific information (like titles, prices, ratings, etc.).
- Print the results nicely in the console.
- Save the results to a **CSV file**.

---

## Technical Requirements:
- Python only (no Jupyter, just VSCode ✅)
- Use `requests` to send HTTP requests.
- Use `BeautifulSoup` from `bs4` to parse HTML.
- Handle possible errors (like if the page doesn't load).
- Save the data using Python’s `csv` module.

---

## Example Target Websites (you can pick one):
- [books.toscrape.com](http://books.toscrape.com/) — (easy and made for practice)
- [quotes.toscrape.com](http://quotes.toscrape.com/) — (good if you want to scrape text)
- Any other simple site (I can help check if it’s good)

---

## Stretch Goals (Optional if you want to make it fancier):
- Allow the user to input a search term (like "fantasy books" or "motivational quotes").
- Save more detailed data (like links, prices, ratings).
- Add command-line arguments (`argparse`) so the user can control what gets scraped.
