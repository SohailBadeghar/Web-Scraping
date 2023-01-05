import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

# set implicit wait time
driver.implicitly_wait(5) # seconds

driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
driver.maximize_window()
#to refresh the browser
driver.refresh()
# identifying the link with link_text locator
driver.find_element(By.LINK_TEXT,"Guaranteed Monthly Payment").click()
#to close the browser
driver.quit()


