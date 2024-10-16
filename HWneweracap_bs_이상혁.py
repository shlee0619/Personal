import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium  import webdriver
from selenium.webdriver.common.by import By
import requests
import numpy as np

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


url = "https://www.neweracapkorea.com"
# al_url = "/shop/shopbrand.html?xcode=031&mcode=002&type=Y&gf_ref=Yz1vU0FlS3M="

driver = webdriver.Chrome()
url = 'https://www.neweracapkorea.com/shop/shopbrand.html?xcode=031&mcode=002&type=Y&gf_ref=Yz1vU0FlS3M='

driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

al_url = []
price = []
name = []
material = []
height = []
brim = []

for i in range(2,4):
    for j in range(1,6):
        time.sleep(1)
        al_url.append(driver.find_element(By.XPATH, f'//*[@id="MS_product"]/table/tbody/tr[{i}]/td[{j}]/div/div/a').get_attribute('href'))


time.sleep(1)


for index, al in enumerate(al_url):
    try:
        time.sleep(1)
        driver.get(al_url[index])
        html = driver.page_source
        soupCap = BeautifulSoup(html, 'html.parser')    
        nx = 'div.info > h3'                
        px = '#price_text'
        infox = '.tb-left'

        time.sleep(1)
        n = soupCap.select_one('div.info > h3')
        p = soupCap.select_one('#price_text')
        price.append(p.string)
        name.append(n.string)
        infos = soupCap.select(infox)
        time.sleep(1)
        material.append(infos[8].string)
        height.append(infos[10].string)
        brim.append(infos[12].string)

        print(price[index], name[index], material[index], height[index], brim[index])
    except Exception as e:
         print(f"Error processing item {index}: {e}")
         

df = pd.DataFrame({
    '모자 이름': name,
    '소재': material,
    '높이': height,
    '챙 길이': brim,
    '가격': price})

df.to_csv('./cap.csv', encoding='cp949', index=True)
print(df)


                                        






time.sleep(1)
driver.quit()
print()
