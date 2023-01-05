import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Practice']").click()
time.sleep(3)

