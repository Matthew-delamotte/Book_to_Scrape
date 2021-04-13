# ----- En dev ------

import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import csv


# def add_info_as_row(list_of_elem, title):
#     with open('product.csv', 'w') as write_info:
#         a = writer(write_info)
#         a.write(title + '\n')
#         a.write(list_of_elem)


# def append_list_as_row(file_name, list_of_elem):
#     # Open file in append mode
#     with open(file_name, 'a+', newline='') as write_obj:
#         # Create a writer object from csv module
#         csv_writer = writer(write_obj)
#         # Add contents of list as last row in the csv file
#         csv_writer.writerow(list_of_elem)


url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
path = html.fromstring(response.content) #


if response.ok:
    with open('product.csv', 'w') as product_out:
        soup = BeautifulSoup(response.text, 'lxml')
        product_description = path.xpath('// *[ @ id = "content_inner"] / article / p / text()')
        product_page_url = url
        title = soup.find('h1')
        # stock_list = soup.find('p', {'class': 'instock availability'}) # -- a revoir --
        stock = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()')
        # print(stock)

        # Add title
        product_out.write('Title\n')
        product_out.write(title.text + '\n\n')

        # Add URL
        product_out.write('Url\n')
        product_out.write(url + '\n\n')

        # Add Stock availability
        a = ''.join(stock)
        b = a.split()
        c = ''.join(b)
        stock_extract = re.findall('\d+', c)  # recherche tous les décimals
        product_out.write('Stock\n')
        product_out.write(str(stock_extract) + ' Disponible\n\n')
        # stock = ''.join(str(e) for e in stock_brut)

        # Add Product description
        description = ''.join(str(e) for e in product_description)
        product_out.write('Description\n')
        product_out.write(description + '\n\n')




