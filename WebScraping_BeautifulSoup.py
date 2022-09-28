
import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import os 

os.chdir('C:/Users/SSG/Downloads/RPA를 이용한 업무자동화/UiPath')
page = requests.get('https://finance.naver.com/item/sise_day.nhn?code=155660')
soup = BeautifulSoup(page.content, 'html.parser')
dates = soup.find_all(class_='tah p10 gray03')
date_list = [d.text for d in dates]
price = soup.find_all(class_='tah p11')
price_list = [p.text for p in price]
close_list = []

for i in range(0,len(price_list),5):
    close_list.append(price_list[i])
close_list

amount_list = []
for i in range(0,len(price_list),5):
    amount_list.append(price_list[i])
amount_list
df = pd.DataFrame({'date':date_list, 'close':close_list, 'amount':amount_list})
df.to_excel('stock.xlsx')