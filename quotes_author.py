from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.findAll(class_ = "text")
authors = soup.findAll(class_ = "author")

for quote, author in zip(quotes, authors):
    print(f'{quote.text + " by " + author.text}')