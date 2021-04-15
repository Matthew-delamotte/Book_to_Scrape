# ----- En dev ------

import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import csv
from category_scraper import book_links

with open('product.csv', 'w', encoding="utf-8") as product_out:
    for link in book_links:
        url = link
        response = requests.get(url)
        path = html.fromstring(response.content)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')

            product_out.write('------------------------------------------------------------ \n\n')
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

            # Add category
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
            product_out.write(image_url + '\n')

            product_out.write('------------------------------------------------------------ \n\n')

    # else:
    #     print("Error fetching page")
    #     exit()