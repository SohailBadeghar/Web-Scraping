import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(3)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH," //button[@id='mousehover']")).perform()
# time.sleep(10)
action.move_to_element(driver.find_element(By.XPATH," /html/body/div[4]/div/fieldset/div/div/a[1]")).click().perform()
time.sleep(10)
