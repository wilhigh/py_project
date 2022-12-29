#Chrome Browser 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 
import os 
import pyperclip

os.chdir('C:/Users/SSG/Downloads/RPA를 이용한 업무자동화/UiPath')

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#driver = webdriver.ChromeOptions(chrome_options = options)
#driver = webdriver.Edge('D:/Python39/Lib/site-packages/selenium/webdriver/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Chrome('D:/Python39/Lib/site-packages/selenium/webdriver/chromedriver_win32/chromedriver.exe', options=options)
#driver.get('http://finance.naver.com/item/sise_day.nhn?code=155660')
url = 'http://10.253.14.99:9000'
driver.get(url)


user_id = "apsharp"
user_passwd = "tlstprP1@#"
element = driver.find_element(By.ID, 'user_login')
element.send_keys(user_id)
element2 = driver.find_element(By.ID, 'user_password')
element2.send_keys(user_passwd)

driver.find_element(By.NAME, 'commit').click()
#lists = driver.find_elements(By.CLASS_NAME, 'p11')
lists = driver.find_elements(By.CLASS_NAME, 'text-plain')

text_lists = []
for i in range(len(lists)):
    pathGitLab = lists[i].text
    pathGitLab = pathGitLab.replace(" ","")
    print(url+"/"+pathGitLab)
    text_lists.append(lists[i].text)
text_lists
df = pd.DataFrame({'export.csv': text_lists})

df.to_csv('export.csv')