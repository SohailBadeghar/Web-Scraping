from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()
time.sleep(5)
action = ActionChains(driver)
#context_click means right click
action.context_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()

# action.double_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()
time.sleep(5)
alert = driver.switch_to.alert
time.sleep(5)
alert.accept()
 