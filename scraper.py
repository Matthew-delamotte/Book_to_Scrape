import requests
from bs4 import BeautifulSoup
import time


# url = 'http://books.toscrape.com/index.html'
# response = requests.get(url)

# if response.ok:
#     # print(response.headers)
#     # print(response.text)
#     links = []
#     soup = BeautifulSoup(response.text, 'lxml')
#     # title = soup.find('title') # --> recupere le premier text dans les balise css title
#     trs = soup.findAll('article') # --> recupere tout les text dans les balise css t
#     # print(len(trs)) # --> Affiche le nombre de resultat
#     # print(str(trs) + '\n') # for tr in trs]
#
#     # for i in trs:
#     #     a = i.find('a')
#     #     link = a['href']
#     #     links.append('http://books.toscrape.com/' + link) # recupere et contatene les liens
#     # print(links)


url = 'http://books.toscrape.com/index.html'
response = requests.get(url)
time.sleep(1) #--> fait une pause de 1sec

if response.ok:
    for i in range(1,51):
        print(url)
        url = 'http://books.toscrape.com/catalogue/page-' + str(i + 1) + '.html'
        response = requests.get(url)

        #
        # if response.ok:
        #     links = []
        #     soup = BeautifulSoup(response.text, 'lxml')
        #     trs = soup.findAll('article')
        #     for i in trs:
        #         a = i.find('a')
        #         link = a['href']
        #         links.append('http://books.toscrape.com/' + link) # recupere et contatene les liens
        #     print(links)




