# ____Passage branch DEV_________

# import requests
# from bs4 import BeautifulSoup
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

import re

string = 'Instock(22available)'
nombres = re.findall('\d+', string) # recherche tous les décimals
print(nombres) # ['34', '65']