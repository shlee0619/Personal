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



for index, al in enumerate(al_url):
    try:
        time.sleep(1)
        driver.get(al_url[index])
        name_xpath = '//*[@id="form1"]/div/h3'                    
        price_xpath = '//*[@id="price_text"]'
        material_xpath = '//*[@id="form1"]/div/div[2]/table/tbody/tr[5]/td/div'
        height_xpath = '//*[@id="form1"]/div/div[2]/table/tbody/tr[6]/td/div'
        brim_xpath = '//*[@id="form1"]/div/div[2]/table/tbody/tr[7]/td/div'
        time.sleep(2)
        price.append(driver.find_element(By.XPATH, price_xpath).text)
        name.append(driver.find_element(By.XPATH, name_xpath).text)
        material.append(driver.find_element(By.XPATH, material_xpath).text)
        height.append(driver.find_element(By.XPATH, height_xpath).text)
        brim.append(driver.find_element(By.XPATH, brim_xpath).text)

        print(price[index], name[index], material[index], height[index], brim[index])
    except Exception as e:
         print(f"Error processing item {index}: {e}")
         

df = pd.DataFrame({
    '모자 이름': name,
    '소재': material,
    '높이': height,
    '챙 길이': brim,
    '가격': price})

print(df)


                                        






time.sleep(1)
driver.quit()
print()
