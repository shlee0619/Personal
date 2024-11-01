import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 웹드라이버 초기화



booknames = []
authors = []


url = f"https://search.kyobobook.co.kr/search?keyword=%EB%8C%80%EC%82%B0%EC%84%B8%EA%B3%84%EB%AC%B8%ED%95%99%EC%B4%9D%EC%84%9C&target=kyobo&gbCode=TOT&page=2&len=100"
driver = webdriver.Chrome()
driver.get(url)
books = driver.find_element(By.XPATH, '//*[@id="shopData_list"]/ul/li')


rows = driver.find_elements(By.XPATH, '//*[@id="shopData_list"]/ul/li')
for i in range(1,101,1):
    try:
        soldout = driver.find_element(By.XPATH, f'//*[@id="shopData_list"]/ul/li[{i}]/div[1]/div[2]/div[5]').text
        
        if (soldout == '품절되었습니다.') or (soldout == '절판되었습니다.') :
            book = driver.find_element(By.XPATH, f'/html/body/div[3]/main/section/div/div/div[4]/div[2]/div/div[2]/div[3]/ul/li[{i}]/div[1]/div[2]/div[2]/div[1]/div/a/span[2]').text
            author = driver.find_element(By.XPATH, f'/html/body/div[3]/main/section/div/div/div[4]/div[2]/div/div[2]/div[3]/ul/li[{i}]/div[1]/div[2]/div[4]/div[1]/div[1]/div/a[1]').text
            print(book, author)
            booknames.append(book)
            authors.append(author)
    except Exception as e:
        print('오류: ', e)
        break




df = pd.DataFrame({
    '책이름': booknames,
    '저자이름': authors
})
    


df.to_csv("대산문학총서_절판.csv", index=False, encoding='utf-8-sig')
print(df)
driver.quit()