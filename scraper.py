# ____Passage branch DEV_________

import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import csv

# import time
#
#
# # url = 'http://books.toscrape.com/index.html'
# # response = requests.get(url)
#
# # if response.ok:
# #     # print(response.headers)
# #     # print(response.text)
# #     links = []
# #     soup = BeautifulSoup(response.text, 'lxml')
# #     # title = soup.find('title') # --> recupere le premier text dans les balise css title
# #     trs = soup.findAll('article') # --> recupere tout les text dans les balise css t
# #     # print(len(trs)) # --> Affiche le nombre de resultat
# #     # print(str(trs) + '\n') # for tr in trs]
# #
# #     # for i in trs:
# #     #     a = i.find('a')
# #     #     link = a['href']
# #     #     links.append('http://books.toscrape.com/' + link) # recupere et contatene les liens
# #     # print(links)
#
# #
# # url = 'http://books.toscrape.com/index.html'
# # response = requests.get(url)
# # links = []
# #
# # # time.sleep(1) #--> fait une pause de 1sec
# #
# # if response.ok:
# #     for i in range(1,51):
# #         print(url)
# #         url = 'http://books.toscrape.com/catalogue/page-' + str(i + 1) + '.html'
# #         response = requests.get(url)
# #         if response.ok:
# #             soup = BeautifulSoup(response.text, 'lxml')
# #             trs = soup.findAll('article')
# #             for i in trs:
# #                 a = i.find('a')
# #                 link = a['href']
# #                 links.append('http://books.toscrape.com/' + link) # recupere et contatene les liens
# #
# # with open('fichier.txt', 'w') as file:
# #     for link in links:
# #         file.write(link + '\n')
# #
# # with open('fichier.txt', 'r') as file:
# #     for raw in file:
# #         print(raw)
# #
# # url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
# # response = requests.get(url)
# # if response.ok:
# #     soup = BeautifulSoup(response.text)
# #     tableau = soup.find('table', {'class': 'table table-striped'})
#
# rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
# rel_soup.a['rel']
# # ['index']
# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)
#
#
# list1 = [1, 2, 3]
# str1 = ''.join(str(e) for e in list1)
# print(str1)
#
# import re
#
# string = 'Instock(22available)'
# nombres = re.findall('\d+', string) # recherche tous les décimals
# print(nombres) # ['34', '65']

# # Add star-rating - WIP
# rating = soup.find('div', {'class': 'col-sm-6 product_main'}).findNext('p').findNext('p').findNext('p')
# rating = rating['class']
# # rating = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]')
# # css_soup = BeautifulSoup('<p class="five star"></p>', 'html.parser')
# # f = css_soup.a['class']
# # print(f) #content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating.Five
# # rating = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]')
# product_out.write('Star Rating\n')
# product_out.write(rating[1] + ' Star(s)\n\n')

# url = 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'
# response = requests.get(url)
# path = html.fromstring(response.content)
#
# if response.status_code != 200:
# 	print("Error fetching page")
# 	exit()
# else:
# 	content = response.content
# #
# soup = BeautifulSoup(response.content, 'html.parser')
# # nb_links = len(soup.find_all('a'))
# # print(f"There are {nb_links} links in this page")
#
# r = soup.find['class']
# print(soup.find['class'])
# # f = soup.find()
# # rel_soup = BeautifulSoup(t, 'html.parser')
# # f = rel_soup.p['class']
# # print(' '.join(str(e) for e in f))

c = ['travel']
book_links = []
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
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

for i in c:
    with open(i + '.csv', 'w', encoding="utf-8") as csv_file:
        fieldnames = ['Product_page_url', 'Universal_ product_code', 'Title', 'Price_including_tax',
                      'Price_excluding_tax', 'Number_available', 'Product_description',
                      'Category', 'Review_rating', 'Image_url']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for link in book_links:
            url = link
            response = requests.get(url)
            path = html.fromstring(response.content)
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Product URL scraping --------------------------
                product_page_url = url # return(url)
                # UPC scraping ----------------------------------
                upc = soup.find('table', {'class': 'table table-striped'}).findNext('td').contents # return(upc[0])
                # Title scraping --------------------------------
                title = soup.find('h1') # return(title.text)
                # Price scraping --------------------------------
                price_incl_tax = soup.find('table', {'class': 'table table-striped'}).findNext('td').findNext(
                    'td').findNext('td').findNext('td').contents # return(price_incl_tax[0])
                price_excl_tax = soup.find('table', {'class': 'table table-striped'}).findNext('td').findNext(
                    'td').findNext('td').contents # return(price_excl_tax[0])
                # Stock scraping --------------------------------
                stock = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()')
                stock = ''.join(stock)
                stock = re.findall('\d+', stock)  # recherche toutes les décimals # write(stock[0])
                # Description scraping --------------------------
                product_description = path.xpath('// *[ @ id = "content_inner"] / article / p / text()')
                description = ''.join(str(e) for e in product_description) # return(description)
                # Category scraping -----------------------------
                category = soup.find('div', {'class': 'page_inner'}).findNext('li').findNext('li').findNext(
                    'li').find('a').contents
                for child in category:
                    category = child # return (category)
                # Rating scraping -------------------------------
                rating = soup.find('div', {'class': 'col-sm-6 product_main'}).findNext('p').findNext('p').findNext('p')
                rating = rating['class'] # return(rating[1]
                # Image URL scraping ----------------------------
                image_url = soup.find('div', class_='item active').find('img')
                image_url = 'http://books.toscrape.com/' + image_url['src'] # return(image_url)

                extract_info = [product_page_url, upc[0], title.text, price_incl_tax[0],
                                price_excl_tax[0], stock[0], description, category, rating[1], image_url]
                wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                wr.writerow(extract_info)

with open('travel.csv', 'r', encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(line)