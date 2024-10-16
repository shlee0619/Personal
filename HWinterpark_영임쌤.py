
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


def scroll_move(element):
    try:
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'end', inline: 'start'});", element)
        #~~[0].scrollIntoView({behavior: 'smooth', block: 'end', inline: 'start'});", element)
    except Exception as ex:
        print(f'scroll_into_view : {ex}')
    

try:
    search_query = "로마"
    driver.get("https://search-travel.interpark.com/search?q=")
    
    search_box = driver.find_element(By.ID, 'divHeaderSearch')
    search_box.click()
    time.sleep(1)  
    txtHeaderInput = driver.find_element(By.ID, 'txtHeaderInput')
    txtHeaderInput.send_keys(search_query)
    time.sleep(5)  
    btnHeaderInput = driver.find_element(By.ID, 'btnHeaderInput')
    btnHeaderInput.click() 
    time.sleep(2)  

    # keyword ='로마'
    # driver.get(f'https://search-travel.interpark.com/search?q={keyword}')
    # time.sleep(5)
    boxList = driver.find_element(by=By.CLASS_NAME, value='boxList')        # ul
    boxItems = boxList.find_elements(by=By.CLASS_NAME, value='boxItem')     # li

    print('인터파크 여행정보 크롤링 출력')
    for item in boxItems:
        infoTitle = item.find_element(by=By.XPATH, value='div/div[2]/div[2]/div[1]/a/h5').text
        infoFlightWay = item.find_element(by=By.XPATH, value='div/div[2]/div[3]/div[1]/p[1]/span').text
        infoDate = item.find_element(by=By.XPATH, value='div/div[2]/div[3]/div[1]/p[2]').text
        infoPrice = item.find_element(by=By.XPATH, value='div/div[2]/div[2]/div[2]/div/p/strong').text
        
        print('여행지 : {}\n{}\n{}\n가격 : {}원\n'.format(infoTitle, infoFlightWay, infoDate, infoPrice)) 
        print('- ' * 70)
        time.sleep(2)
        scroll_move(item)
        

except(Exception) as ex:
    print('에러이유 = ',ex)


time.sleep(10)
driver.quit()
print()
