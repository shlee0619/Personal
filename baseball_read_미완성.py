import time
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


print('kbo 크롤링 시작')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome()
url = "https://www.koreabaseball.com/Futures/Schedule/GameList.aspx"
driver.get(url)

#날짜 설정
year_select = Select(driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlYear'))
month_select = Select(driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlMonth'))
year_select.select_by_value('2020')
month_select.select_by_value('05')
game_list = driver.find_elements(By.ID, 'cphContents_cphContents_cphContents_udpRecord')


def isExistXpath(game, xpath):
    try:
        game.find_element(By.XPATH, xpath)
        return True
    except:
        return False




Date = []
Ballpark = []
AwayTeam = []
HomeTeam = []
AwayTeamResult = []
HomeTeamResult = []
Away = []
Home = []

for idx, game in enumerate(game_list, start=1):
    time.sleep(1)
    
    Date.append(game.find_element(By.XPATH, "//*[@id=\"cphContents_cphContents_cphContents_rptGameList_lblGameDate_0\"]"))
    #/html/body/form/div[3]/section/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]
    Ballpark.append(game.find_element(By.CLASS_NAME, "ballpark"))
    AwayTeam.append(game.find_element(By.XPATH, f"table/tbody/tr[{idx}]/td[2]/span[1]"))
    HomeTeam.append(game.find_element(By.XPATH, f"table/tbody/tr[{idx}]/td[2]/span[2]"))
    AwayTeamResult.append(game.find_element(By.XPATH, f"table/tbody/tr[{idx}]/td[2]/em/span[1]"))
    HomeTeamResult.append(game.find_element(By.XPATH, f"table/tbody/tr[{idx}]]/td[2]/em/span[3]"))


df = pd.DataFrame({
    'Date': Date,
    '구장': Ballpark,
    '원정팀': AwayTeam,
    '원정팀점수': AwayTeamResult,
    '홈팀': HomeTeam,
    '홈팀점수': HomeTeamResult,
    })
print(df)

'''
year_select = Select(driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlYear'))
month_select = Select(driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlMonth'))

year_select.select_by_value('2021')
month_select.select_by_value('05')
time.sleep(3)

Date = []
Ground = []
Team = []




#각 경기 분석

for idx, game in enumerate(game_list):





print(game_list)
'''