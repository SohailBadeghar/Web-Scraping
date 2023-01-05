import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH," //input[@id='name']").send_keys("Sohail Badeghar")
time.sleep(2)
driver.find_element(By.XPATH," //input[@id='alertbtn']").click()


alert = driver.switch_to.alert
time.sleep(5)
print(alert.text)
assert "Sohail Badeghar" in alert.text
alert.accept()
