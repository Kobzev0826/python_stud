# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:40:42 2020

@author: User
"""
import requests
from bs4 import BeautifulSoup,SoupStrainer
import pandas as pd

from globus_items import test

base_url = 'https://www.globus.ru'

#полчение ссылок каталога
catalog_url = 'https://www.globus.ru/catalog/'
catalog = requests.get(catalog_url,timeout=(10, 10)) #отправляем HTTP запрос и получаем результат
soup = BeautifulSoup(catalog.text)

#Получаем список ссылок с главной страницы
list_urls = []
for item in soup.find_all('div', {'class': 'js-p-m-m__item p-m-m__item'}):
    for k in item.find_all('a'):
        #link = k.get('href')
        link = str(k.get('href'))
        list_urls.append(link)
    #    print(link)
    #print('--------------')

print(list_urls)
print('--------------------')

#начинаем поиск по каждому каталогу 


#gl.
test()

