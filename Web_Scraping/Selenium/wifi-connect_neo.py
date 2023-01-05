from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services = Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("http://10.0.30.9:8090/httpclient.html")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("sohail.badeghar")
time.sleep(5)
driver.find_element(By.NAME, "password").send_keys("Ne0@9244")
time.sleep(5)

# how to click on the button
driver.find_element(By.ID, "logincaption").click()

time.sleep(10)
