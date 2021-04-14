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


url = 'http://books.toscrape.com/catalogue/olio_984/index.html'
response = requests.get(url)
path = html.fromstring(response.content) #


if response.ok:
    with open('product.csv', 'w', encoding="utf-8") as product_out:
        soup = BeautifulSoup(response.text, 'html.parser')
        # stock_list = soup.find('p', {'class': 'instock availability'}) # -- a revoir --

        # Add title
        title = soup.find('h1')
        product_out.write('Title\n')
        product_out.write(title.text + '\n\n')

        # Add URL
        product_page_url = url
        product_out.write('Url\n')
        product_out.write(url + '\n\n')

        # Add Stock availability
        stock = path.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()')
        stock = ''.join(stock)
        stock = re.findall('\d+', stock) # recherche toutes les décimals
        product_out.write('Stock\n')
        product_out.write(stock[0] + ' Disponible\n\n')
        # stock = ''.join(str(e) for e in stock_brut)

        # Add Product description
        product_description = path.xpath('// *[ @ id = "content_inner"] / article / p / text()')
        description = ''.join(str(e) for e in product_description)
        product_out.write('Description\n')
        product_out.write(description + '\n\n')

        # Add star-rating
        rating = soup.find('div', {'class': 'col-sm-6 product_main'}).findNext('p').findNext('p').findNext('p')
        rating = rating['class']
        product_out.write('Star Rating\n')
        product_out.write(rating[1] + ' Star(s)\n\n')

        # Add catégory
        category = soup.find('div', {'class': 'page_inner'}).findNext('li').findNext('li').findNext('li').find('a').contents
        product_out.write('Category\n')
        for child in category:
            product_out.write(child + ' ')
        product_out.write('\n\n')


        #  Add UPC
        upc = soup.find('table', {'class': 'table table-striped'}).findNext('td').contents
        product_out.write('UPC\n')
        product_out.write(upc[0] + '\n\n')


        # Add Price including tax
        price_incl_tax = soup.find('table', {'class': 'table table-striped'}).findNext('td').findNext('td').findNext('td').findNext('td').contents
        product_out.write('Price (incl. Tax)\n')
        product_out.write(price_incl_tax[0] + '\n\n')

        # Add Price excluding tax
        price_excl_tax = soup.find('table', {'class': 'table table-striped'}).findNext('td').findNext('td').findNext('td').contents
        product_out.write('Price (excl. Tax)\n')
        product_out.write(price_excl_tax[0] + '\n\n')

        # Add image_url
        image_url = soup.find('div', class_='item active').find('img')
        image_url = 'http://books.toscrape.com/' + image_url['src']
        product_out.write('Image Url)\n')
        product_out.write(image_url + '\n\n')

