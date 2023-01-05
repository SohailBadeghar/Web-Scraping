from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5) 
driver.find_element(By.CSS_SELECTOR,("input[value='radio2']")).click()
driver.find_element(By.CSS_SELECTOR,("#name")).send_keys("Sohail Badeghar")

time.sleep(5) 