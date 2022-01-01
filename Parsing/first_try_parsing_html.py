# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:47:41 2020
tru to parsing html
@author: VAK
"""
from bs4 import BeautifulSoup
import pandas as pd

#функция для выделения стоимости из контейнера <div> связано с невозможностью воспользоваться методом text
def price_from_string(s):
    word_list=str(s).split()
    print(word_list)
    for i in range(len(word_list)):
        
        if i == 3:   
            return(float(word_list[i]))


result=pd.DataFrame(columns=['Name','Aticule','Price'])

with open ('Крупы_ купить оптом в METRO Cash and Carry Москва.html',encoding='utf-8') as f:
    contens = f.read()
    soup = BeautifulSoup(contens)
    
    tables=soup.find_all('div',{'class':'catalog-item'})
    links=[]
    for item in tables:
        #print('------------------------------------')
        text = item.find('a',{'class':'catalog-item_name'}).text
        art = item.find('div',{'class':'catalog-item_article'}).text[item.find('div',{'class':'catalog-item_article'}).text.find('.')+1:]
        price = price_from_string(item.find('div','catalog-item_price-lvl_current'))
        if price is None:
            price =price_from_string(item.find('div','catalog-item_price-current')) 
        result = result.append(pd.DataFrame([[text,int(art),price]], columns= ['Name','Aticule','Price']))
        

print('------------------------------------------')
print(result.head(15))
print('end')
print('--------------------------------------------')
result.to_excel('Parsing_Cash_and_Carry_result.xlsx')