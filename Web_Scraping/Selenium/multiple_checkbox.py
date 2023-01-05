'''
In this script We selecting the multiple checkboxex. for that you have to create xpath which will be 
common for all checkboxes then use for loop to click all .
'''


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox == checkboxes[1]:
        pass
    else:
        checkbox.click()
print(len(checkboxes))
time.sleep(5)


















