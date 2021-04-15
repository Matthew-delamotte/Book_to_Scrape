import requests
from bs4 import BeautifulSoup
from main import url_category

book_links = []
url = url_category
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
a_books = soup.find_all('h3')
for i in a_books:
    b = i.find('a')
    link = b['href']
    link = ''.join(link)
    link = link[9:]
    book_links.append('http://books.toscrape.com/catalogue/' + link)

page = 2
while response.status_code == 200:
    search = url[:-10] + 'page-' + str(page) + '.html'
    page += 1
    response = requests.get(search)
    soup = BeautifulSoup(response.text, 'lxml')
    a_books = soup.find_all('h3')
    for i in a_books:
        b = i.find('a')
        link = [b.get('href')]
        link = ''.join(link)
        link = link[9:]
        book_links.append('http://books.toscrape.com/catalogue/' + link)