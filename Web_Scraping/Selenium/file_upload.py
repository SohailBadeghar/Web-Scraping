'''
Locate elements with tagname "input" then in the send_keys,
gives the complete path of the file.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("/home/neosoft/Pictures/iphone14.jpg")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@id='file-submit']").click()
time.sleep(2)