# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:19:07 2020

@author: whiteskinblacksoul
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


#функция для выделения стоимости из контейнера <div> связано с невозможностью воспользоваться методом text
def price_from_string(s):
    word_list=str(s).split()
    #print(word_list)
    for i in range(len(word_list)):
        
        if i == 3:   
            return(float(word_list[i]))


print('--------------------------------------')

bank_id = 1771062 #ID банка на сайте banki.ru
page=1
max_page=10

url = 'https://msk.metro-cc.ru/category/bakaleya/krupy-bobovye'

#пробуем делать запросы 
'''
print('введите запрос:')
request=input()

url='https://msk.metro-cc.ru/search?q='+str(request)
'''
#url='https://www.globus.ru/catalog/'
print(url)


result = pd.DataFrame()

r = requests.get(url,timeout=(10, 10)) #отправляем HTTP запрос и получаем результат
#записиваем в файл для отладки 
f=open(r'file_request.html',"wb") #открываем файл для записи, в режиме wb
f.write(r.content) #записываем содержимое в файл; как видите - content запроса
f.close()


soup = BeautifulSoup(r.text) #Отправляем полученную страницу в библиотеку для парсинга

tables=soup.find_all('div', {'class': 'catalog-item'}) 
print(tables)
for item in tables:
    '''
    names=item.find('a', {'class': 'catalog-item_name'}).text
    print('~~~~~~~~~~~~~~~~~~')
    print(names)#.decode('utf-8'))
    article = item.find('div',{'class':'catalog-item_article'})
    print('art= ', article)
    '''
    text = item.find('a',{'class':'catalog-item_name'}).text
    art = item.find('div',{'class':'catalog-item_article'}).text[item.find('div',{'class':'catalog-item_article'}).text.find('.')+1:]
    price = price_from_string(item.find('div','catalog-item_price-lvl_current'))
    if price is None:
        price =price_from_string(item.find('div','catalog-item_price-current')) 
    result = result.append(pd.DataFrame([[text,int(art),price]], columns= ['Name','Aticule','Price']))

print('END')
print('--------------------------------------------')
print(result.head())
result.to_excel('Parsing_Cash_and_Carry_result.xlsx')