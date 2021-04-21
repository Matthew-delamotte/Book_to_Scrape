import string
import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import csv
import os
from helpers import format_category_name
from helpers import clean_filename
from helpers import found_book_link

# permanante variable
category_list = []
url_list = []
data = {}

path_demand = input("Entrer l'adresse du repertoire de sauvegarde: ")

# add url website
url_website = 'http://books.toscrape.com/'
response = requests.get(url_website)
soup = BeautifulSoup(response.text, 'lxml')
# take all category url in list
url_link = soup.find('ul', {'class': 'nav nav-list'}).findAll('ul')
for i in url_link:
    b = i.findAll('a')
    for link in b:
        category_list.append(format_category_name(link))
        url_list.append(link.get('href'))

# concatenate links page for category + add it in list
url_category = []
for link in url_list:
    url_category.append(url_website + link) # add link to category

data = dict(zip(url_category, category_list)) # link category with is url in dict.

# extract all book link from dict item.
for category_link, value in data.items():
    print(category_link)           # console check if everything run good
    book_links = []                                 # create list for book url
    response = requests.get(category_link)
    soup = BeautifulSoup(response.text, 'lxml')
    a_books = soup.find_all('h3')
    for i in a_books:
        book_links.append('http://books.toscrape.com/catalogue/' + found_book_link(i)) # Append link of first of category

    page = 1
    while response.status_code == 200:  # verify if url is valid, if not restart new category page
        search = category_link[:-10] + 'page-' + str(page) + '.html' # Concatenate link of category and page numbers for next url
        page += 1                                                    # Add one to page for concatenate next page
        response = requests.get(search)
        soup = BeautifulSoup(response.text, 'lxml')
        a_books = soup.find_all('h3')
        for i in a_books:
            book_links.append('http://books.toscrape.com/catalogue/' + found_book_link(i)) # Found all book of page and add it to list

    print(value + '______________________________.......')
    path = path_demand + '\\book_to_scrap_csv\\' + value
    path_image = path_demand + '\\book_to_scrap_csv\\' + value + '\\image\\'
    filepath = os.path.join(path, value + '.csv')
    if not os.path.exists(path):
        os.makedirs(path)
    # console check if category name is good
    with open(filepath, 'w+', encoding="utf-8", newline='') as csv_file:   # create csv file of value name (write mode)
        fieldnames = ['Product_page_url', 'Universal_ product_code', 'Title', 'Price_including_tax',
                      'Price_excluding_tax', 'Number_available', 'Product_description',
                      'Category', 'Review_rating', 'Image_url']         # add field names to csv file
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader() # write field names for csv file
        for link in book_links: # scrap info of book page
            url = link
            response = requests.get(url)
            path = html.fromstring(response.content)
            soup = BeautifulSoup(response.text, 'lxml')
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
                # Category scraping -----------------------------
                category = soup.find('div', {'class': 'page_inner'}).findNext('li').findNext('li').findNext(
                    'li').find('a').contents
                for child in category:
                    category = child # return (category)
                # Rating scraping -------------------------------
                rating = soup.find('div', {'class': 'col-sm-6 product_main'}).findNext('p').findNext('p').findNext('p')
                rating = rating['class'] # return (rating[1])
                # Image URL scraping ----------------------------
                image_url = soup.find('div', class_='item active').find('img')
                image_url = 'http://books.toscrape.com/' + image_url['src'] # return(image_url)

                # make list if all extract info
                extract_info = [product_page_url, upc[0], title.text, price_incl_tax[0],
                                price_excl_tax[0], stock[0], product_description, category, rating[1], image_url]
                print(extract_info) # extract info check
                # write info in csv file
                wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                wr.writerow(extract_info)

                 # Download image of book url
                if not os.path.exists(path_image):
                    os.makedirs(path_image)
                req = requests.get(image_url, stream=True)
                with open(path_image + clean_filename(title.text) + '.' + image_url.split('.')[-1], 'wb+') as img_dl: # Split l'url avec tout les '.', et commence la chaine par la dernier occurence.
                    img_dl.write(req.content)
                img_dl.close()
    csv_file.close()
