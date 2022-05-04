#Utilize o código do Webscraping e utilize-o como exemplo para desenvolver a coleta de informações de outra letra de sua preferência.#O código precisa ser entregue através de link do Github;
# No github deve constar o código e o arquivo em csv que você coletou;
# Vamos colocar também, os créditos do autor do projeto (que não foi o professor): Lisa Tagliaferri - Developer and author at DigitalOcean.

#'''
# 1 - Criar uma variável de ambiente
# 2 - Instalar o requests e o BeautifulSoup4
# '''

print("******************************************************************")
print("*******ALTERAÇÃO DO CÓDIGO WEBSCRAPING - LISA TAGLIAFERRI*********")
print("******************************************************************")

import requests
import csv
from bs4 import BeautifulSoup


f = csv.writer(open('r-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(5, 15):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anR' + str(i) + '.htm'
    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links])