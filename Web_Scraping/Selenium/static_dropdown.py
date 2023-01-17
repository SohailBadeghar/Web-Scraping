'''
In this script we will see , how to select static dropdwon, for that 
import select object, give locator inside it, keep this in one varible and use
Select Functions.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
static_dropdown = Select(driver.find_element(By.XPATH," //select[@id='dropdown-class-example']"))
time.sleep(2)

'''
Three methods of Select . Using these we can catch them.
'''
static_dropdown.select_by_visible_text("Option3")
time.sleep(5)

static_dropdown.select_by_index(2)
time.sleep(5)

static_dropdown.select_by_value("option1")

print(" Process is completed.....")
time.sleep(4)

