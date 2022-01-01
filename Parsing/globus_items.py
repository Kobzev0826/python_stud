# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:58:23 2020

@author: User
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def test():
    print('GLOBUS_ITEMS_HERE')


def navigation_globus(soup):
    link = soup.find_all('a',{'class' : 'next js-navigation__page'})#.get('href')
    for item in link: 
        return item.get('href')

def find_products(url):
        result = pd.DataFrame()
        link = 1
        while link != 'None':
            print(link)
            r = requests.get(url,timeout=(100, 100))
            
            soup = BeautifulSoup(r.text) #Отправляем полученную страницу в библиотеку для парсинга

            tables=soup.find_all('div', {'class': 'pim-list__item-content'}) 
        #print(tables)
            for item in tables:
                text = item.find('div',{'class':'pim-list__item-title js-crop-text'}).text
                price_main = item.find('span',{'class':'pim-list__item-price-actual-main'}).text
                
                if price_main.isalnum():
                    price = float(price_main)+float(item.find('span',{'class':'pim-list__item-price-actual-sub'}).text)/100
                else:
                    price= float(price_main.split()[-2])*1000+float(price_main.split()[-1])+float(item.find('span',{'class':'pim-list__item-price-actual-sub'}).text)/100
                #print(text)
                #print(price)
                
                result = result.append(pd.DataFrame([[text.strip(),price]], columns= ['Name','Price']))
                
            #print('~~~~~~~~')
            link = str(navigation_globus(soup))
            #print(link)
            
            url =  'https://www.globus.ru' + link  
            #print(url)
            #print('~~~~~~~~~~')
        
                 
        return result
print('_____________________')

#url = 'https://www.globus.ru/catalog/uchis-vsegda-uchis-vezde/?page=41'
#baseurl = 'https://www.globus.ru'


    
#pd = find_products(url)
#print(pd.head())
#pd.to_excel('Parsing_Globus_result.xlsx')
