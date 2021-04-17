# ____Passage branch DEV_________

import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import csv
import os

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


# permanante variable
category_list = []
url_list = []
data = {}


# add url website
url_website = 'http://books.toscrape.com/'
response = requests.get(url_website)
soup = BeautifulSoup(response.text, 'lxml')
# take all category url in list
url_link = soup.find('ul', {'class': 'nav nav-list'}).findAll('ul')
for i in url_link:
    b = i.findAll('a')
    for link in b:
        category_name = link.contents
        category_name = ''.join(category_name)
        category_name = category_name.strip()
        category_list.append(category_name)
        url_list.append(link.get('href'))

# concatenate links page for category + add it in list
url_category = []
for link in url_list:
    url_category.append(url_website + link) # add link to category

data = dict(zip(url_category, category_list)) # link category with is url in dict.

# extract all book link from dict item.
for category_link, value in data.items():
    print(category_link)                            # console check if everything run good
    book_links = []                                 # create list for book url
    response = requests.get(category_link)
    soup = BeautifulSoup(response.text, 'lxml')
    a_books = soup.find_all('h3')
    for h in a_books:
        b = h.find('a')
        link = b['href']
        link = ''.join(link)
        link = link[9:]
        book_links.append('http://books.toscrape.com/catalogue/' + link) # Append link of first of category

    page = 1
    while response.status_code == 200:  # verify if url is valid, if not restart new category page
        search = category_link[:-10] + 'page-' + str(page) + '.html' # Concatenate link of category and page numbers for next url
        page += 1                                                    # Add one to page for concatenate next page
        response = requests.get(search)
        soup = BeautifulSoup(response.text, 'lxml')
        a_books = soup.find_all('h3')
        for i in a_books:
            b = i.find('a')
            link = [b.get('href')]
            link = ''.join(link)
            link = link[9:]
            book_links.append('http://books.toscrape.com/catalogue/' + link) # Found all book of page and add it to list

    print(value)
    path = 'D:\\Project Files\\Projet_2\\Book_to_Scrape\\csv_folder' + '\\' + value
    p = 'D:\\Project Files\\Projet_2\\Book_to_Scrape\\csv_folder' + '\\' + value + '\\'
    filepath = os.path.join(path, value + '.csv')
    if not os.path.exists(path):
        os.makedirs(path)
    # f = open(filepath, "a")  # ??
    # console check if category name is good
    with open(filepath, 'w', encoding="utf-8") as csv_file:           # create csv file of value name (write mode)
        with open(filepath, 'r', encoding="utf-8") as file_reader:    # (read mode)
            fieldnames = ['Product_page_url', 'Universal_ product_code', 'Title', 'Price_including_tax',
                          'Price_excluding_tax', 'Number_available', 'Product_description',
                          'Category', 'Review_rating', 'Image_url']         # add field names to csv file
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader() # write field names for csv file
            v = []
            for link in book_links: # scrap info of book page
                url = link
                response = requests.get(url)
                path = html.fromstring(response.content)
                soup = BeautifulSoup(response.text, 'lxml')
                d = soup.find('article', {'class': "product_page"}).findNext('p').findNext('p').findNext('p').findNext('p').text
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
                    product_description = soup.find('article', {'class': "product_page"}).findNext('p').findNext('p').findNext('p').findNext(
                        'p').text
                    # product_description = path.xpath('// *[ @ id = "content_inner"] / article / p / text()')
                    # description = ''.join(str(e) for e in product_description) # return(description)
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
                                    price_excl_tax[0], stock[0], product_description, category, rating[1], image_url]
                    print(extract_info)
                    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                    wr.writerow(extract_info)

                    img_download = requests.get(image_url)
                    img = open(p + title.text + '.jpg', "wb")
                    img.write(img_download.content)