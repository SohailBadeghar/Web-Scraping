'''
Create Xpath which will be commomn for all suggestions ,
then use for loop to select function.
'''


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://www.cleartrip.com/flights")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='w-100p fs-4 fw-500 c-neutral-500']").send_keys('del')
time.sleep(2)
from_airport = driver.find_elements(By.XPATH,"//div[@class='dropdown p-absolute t-13 ln-1 w-100p']/ul/li/div/div/following-sibling::div/p")

for airport in from_airport:
    if airport.text == 'New Delhi, IN - Indira Gandhi Airport (DEL)':
        time.sleep(5)
        airport.click()
    else:
        pass
time.sleep(5)
