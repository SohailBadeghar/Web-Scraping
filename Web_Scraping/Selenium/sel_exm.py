'''
In this script we are using navigation to get, and locators and also some actions
send_keys(), click(), clear(), text are used.
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)
#navigations we can navigate to perticuler browser.
# driver.get("https://emp.neosofttech.com/")  
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(5)

copy_texts = driver.find_element(By.ID,"mousehover").text
print(copy_texts)
username = "sohail.badeghar"
driver.find_element(By.ID, "name").send_keys(username)

# driver.find_element(By.NAME, "enter-name").send_keys(username)
# driver.find_element(By.CLASS_NAME, "inputs").send_keys(username)

#how to click on the button 
driver.find_element(By.ID, "alertbtn").click()

time.sleep(10)

driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material" ).click()