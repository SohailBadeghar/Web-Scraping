'''
driver.switch_to_frame('x'),x can be id value, class value,name value or driver.
find_element things also.
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services = Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)
# driver.implicitly_wait(60)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# time.sleep(5)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']"))

driver.find_element(By.XPATH,"//ul[@class='navigation clearfix']/li[6]/a").click()
# time.sleep(5)
driver.switch_to.default_content()
# time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sohail Badeghar")
# time.sleep(3)
