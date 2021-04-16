# # ____Passage branch DEV_________
#
# # -*- coding: utf8 -*-
# import json
# import random
#
# # # Give a Json file and return a List
# # def read_values_from_json(path, key):
# #     values = []
# #     with open(path) as f:
# #         data = json.load(f)
# #         for entry in data:
# #             values.append(entry[key])
# #         return values
# #
# # # Give a json and return a list
# # def clean_strings(sentences):
# #     cleaned = []
# #     # Store quotes on a list. Create an empty list and add each sentence one by one.
# #     for sentence in sentences:
# #         # Clean quotes from whitespace and so on
# #         clean_sentence = sentence.strip()
# #         # don't use extend as it adds each letter one by one!
# #         cleaned.append(clean_sentence)
# #     return cleaned
# #
# # # Return a random item in a list
# # def random_item_in(object_list):
# #     rand_numb = random.randint(0, len(object_list) - 1)
# #     return object_list[rand_numb]
# #
# # # Return a random value from a json file
# # def random_value(source_path, key):
# #     all_values = read_values_from_json(source_path, key)
# #     clean_values = clean_strings(all_values)
# #     return random_item_in(clean_values)
# #
# #
# # #####################
# # ###### QUOTES #######
# # #####################
# #
# # # Gather quotes from San Antonio
# #
# # def random_quote():
# #     return random_value('quotes.json', 'quote')
# #
# # ######################
# # #### CHARACTERS ######
# # ######################
# #
# # # Gather characters from Wikipedia
# #
# # def random_character():
# #     return random_value('characters.json', 'character')
# #
# #
# # ######################
# # #### INTERACTION ######
# # ######################
# #
# # # Print a random sentence.
# #
# # def print_random_sentence():
# #     rand_quote = random_quote()
# #     rand_character = random_character()
# #     print(">>>> {} a dit : {}".format(rand_character, rand_quote))
# #
# # def main_loop():
# #     while True:
# #         print_random_sentence()
# #         message = ('Voulez-vous voir une autre citation ?'
# #                    'Pour sortir du programme, tapez [B].')
# #         choice = input(message).upper()
# #         if choice == 'B':
# #             break
# #             # This will stop the loop!
# #
# # if __name__ == '__main__':
# #     main_loop()
#
#
# import csv
#
# # f = open('test.csv')
# # fichierCSV = csv.reader(f)
# #
# # # for ligne in fichierCSV:
# # #     print(ligne)
# # #
# # ligneX = []
# # ligneY = []
# #
# # for ligne in fichierCSV:
# #     x = ligne[0]
# #     # y = ligne[1]
# #     ligneX.append(x)
# #     # ligneY.append(y)
# #
# # print(ligneX)
# # print(ligne)
#
#
#
#

import requests
from bs4 import BeautifulSoup
from lxml import html
import re
#
# # Sort liens des pages de catégorie
# category_list = []
# url_list = []
#
# url_website = 'http://books.toscrape.com/'
# response = requests.get(url_website)
# soup = BeautifulSoup(response.text, 'lxml')
#
#
# tag = soup.find('ul', {'class': 'nav nav-list'}).findNext('ul').findAll('a')
# url_link = soup.find('ul', {'class': 'nav nav-list'}).findAll('ul')
# for i in url_link:
#     b = i.findAll('a')
#     for link in b:
#         # category_name = link.contents
#         # category_name = ''.join(category_name)
#         # category_name = category_name.strip()
#         # category_list.append(category_name)
#         url_list.append(link.get('href'))
#
# # Sort liens premiere page de la catégorie
# for link in url_list:
#     url_category = url_website + link
#     # --------------------------------------------------------------------------------------------------
#     book_links = []
#     url = url_category
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     a_books = soup.find_all('h3')
#     for i in a_books:
#         b = i.find('a')
#         link = b['href']
#         link = ''.join(link)
#         link = link[9:]
#         book_links.append('http://books.toscrape.com/catalogue/' + link)
#
# # Sort tout les liens page catalogue
#     page = 2
#     while response.status_code == 200:
#         search = url[:-10] + 'page-' + str(page) + '.html'
#         page += 1
#         response = requests.get(search)
#         soup = BeautifulSoup(response.text, 'lxml')
#         a_books = soup.find_all('h3')
#         for i in a_books:
#             b = i.find('a')
#             link = [b.get('href')]
#             link = ''.join(link)
#             link = link[9:]
#             book_links.append('http://books.toscrape.com/catalogue/' + link)
#
# # Scrap la page et write sur product.csv
#     with open('product.csv', 'w', encoding="utf-8") as product_out:
#         for link in book_links:
#             url = link
#             response = requests.get(url)
#             path = html.fromstring(response.content)
#             if response.ok:
#                 soup = BeautifulSoup(response.text, 'html.parser')
#
#                 product_out.write('------------------------------------------------------------ \n\n')
#                 # Add title
#                 title = soup.find('h1')
#                 product_out.write('Title\n')
#                 product_out.write(title.text + '\n\n')
#
#                 # Add URL
#                 product_page_url = url
#                 product_out.write('Url\n')
#                 product_out.write(url + '\n\n')
#
#                 # Add Stock availability
#                 stock = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()')
#                 stock = ''.join(stock)
#                 stock = re.findall('\d+', stock)  # recherche toutes les décimals
#                 product_out.write('Stock\n')
#                 product_out.write(stock[0] + ' Disponible\n\n')
#
#                 # Add Product description
#                 product_description = path.xpath('// *[ @ id = "content_inner"] / article / p / text()')
#                 description = ''.join(str(e) for e in product_description)
#                 product_out.write('Description\n')
#                 product_out.write(description + '\n\n')
#
#                 # Add star-rating
#                 rating = soup.find('div', {'class': 'col-sm-6 product_main'}).findNext('p').findNext('p').findNext('p')
#                 rating = rating['class']
#                 product_out.write('Star Rating\n')
#                 product_out.write(rating[1] + ' Star(s)\n\n')
#
#                 # Add category
#                 category = soup.find('div', {'class': 'page_inner'}).findNext('li').findNext('li').findNext('li').find(
#                     'a').contents
#                 product_out.write('Category\n')
#                 for child in category:
#                     product_out.write(child + ' ')
#                 product_out.write('\n\n')
#
#                 #  Add UPC
#                 upc = soup.find('table', {'class': 'table table-striped'}).findNext('td').contents
#                 product_out.write('UPC\n')
#                 product_out.write(upc[0] + '\n\n')
#
#                 # Add Price including tax
#                 price_incl_tax = soup.find('table', {'class': 'table table-striped'}).findNext('td').findNext(
#                     'td').findNext('td').findNext('td').contents
#                 product_out.write('Price (incl. Tax)\n')
#                 product_out.write(price_incl_tax[0] + '\n\n')
#
#                 # Add Price excluding tax
#                 price_excl_tax = soup.find('table', {'class': 'table table-striped'}).findNext('td').findNext(
#                     'td').findNext('td').contents
#                 product_out.write('Price (excl. Tax)\n')
#                 product_out.write(price_excl_tax[0] + '\n\n')
#
#                 # Add image_url
#                 image_url = soup.find('div', class_='item active').find('img')
#                 image_url = 'http://books.toscrape.com/' + image_url['src']
#                 product_out.write('Image Url)\n')
#                 product_out.write(image_url + '\n')
#
#                 product_out.write('------------------------------------------------------------ \n\n')
#
#             else:
#                 print('page error')
#                 exit()
# data = dict(zip(category_list, url_list))
#
# if response.status_code != 200:
#     print("Error, Website disconnected")
#     exit()
# else:
#     print('Connected ------ ')
#     print('---------- Welcome to scrap script for Book_to_Scrap ----------\n')
#     print('Category list: ')
#     for key, value in data.items():
#         print(key)
#     print('Please choice category to scrap or write all for scrap all website:')
#     input = input()
#     print(f'You choice {input}.\n\nScrap in progress please wait......')
#     input = input.lower()
#
#     for url in url_list:
#         if input == 'travel':
#             url = soup.find('a', href="catalogue/category/books/travel_2/index.html")
#             url = url_website + str(url.get('href'))
#         elif input == 'mystery':
#             url = soup.find('a', href="catalogue/category/books/mystery_3/index.html")
#             url = url_website + str(url.get('href'))
category_list = []
url_list = []

url_website = 'http://books.toscrape.com/'
response = requests.get(url_website)
soup = BeautifulSoup(response.text, 'lxml')

tag = soup.find('ul', {'class': 'nav nav-list'}).findNext('ul').findAll('a')
url_link = soup.find('ul', {'class': 'nav nav-list'}).findAll('ul')
for i in url_link:
    b = i.findAll('a')
    for link in b:
        category_name = link.contents
        category_name = ''.join(category_name)
        category_name = category_name.strip()
        category_list.append(category_name)
        url_list.append(link.get('href'))

    for value in category_list:
        print(value)
