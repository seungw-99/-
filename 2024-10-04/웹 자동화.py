import time

import pyperclip
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #크롬을 키는 함수
driver.implicitly_wait(10) #페이지를 로딩될때까지 기다려주는거에요
driver.maximize_window() #전체화면으로 실행

driver.get('https://www.naver.com/')
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys('강남 맛집') # 클릭하기
driver.find_element(By.XPATH,'//*[@id="search-btn"]').click()

Subject_List = driver.find_elements(By.CSS_SELECTOR,'span.lnk_tit')
for idx, subject in enumerate(Subject_List, start=1):
    print(f"{idx}위: {subject.text}")


# driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click() # 클릭하기
# driver.find_element(By.XPATH,'//*[@id="account"]/div/a').clear() # 안에 있는 데이터를 지우는코드
# driver.find_element(By.XPATH,'//*[@id="account"]/div/a').send_keys("안녕하세요") # Keyboard 입력



