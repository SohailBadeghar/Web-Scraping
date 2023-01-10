import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
tab1 = driver.window_handles[1]
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
tab2 = driver.window_handles[2]

driver.switch_to.window(tab1)

driver.find_element(By.XPATH,"//div[@class='navbar-collapse collapse clearfix']/ul/li[7]/a").click()

driver.switch_to.window(tab2) 
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//a[normalize-space()='Practice']").click()
time.sleep(5)

