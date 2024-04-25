from bs4 import BeautifulSoup
import requests
import csv

url = 'https://quotes.toscrape.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.findAll(class_ = "text")
authors = soup.findAll(class_ = "author")

# create file and writing into it
f = open('scraped_quotes.csv', 'wt')
writer = csv.writer(f)
writer.writerow(["Quotes", "Authors"])

# Loop through quotes and authors
for quote, author in zip(quotes, authors):
    print(f'{quote.text + " , " + author.text}')
    writer.writerow([quote.text, author.text])
f.close()
