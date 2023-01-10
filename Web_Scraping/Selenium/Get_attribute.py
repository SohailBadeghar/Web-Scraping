'''
In this script we can get the value or placeholder text we can access by the get attribute method.
driver.find_element(By.XPATH,"").get_attribute("attribute name").
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services = Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
text = driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("placeholder")
print(text)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sohail Badeghar")
time.sleep(5)
textfill = driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("value")
print(textfill)
time.sleep(5)
whitetext = driver.find_element(By.XPATH,"//legend[normalize-space()='Switch To Alert Example']").text
print(whitetext)
time.sleep(3)
