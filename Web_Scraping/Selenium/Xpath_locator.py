from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)

# Attribute and Value  : //tagname[@attribute ='value']
driver.find_element(By.XPATH,"//*[@id='radio-btn-example']/fieldset/label[3]/input").click()
time.sleep(2)

#text : //tagname[text()= 'type text here']
a = driver.find_element(By.XPATH,"//legend[text()='Checkbox Example']").text
print(a)

#parents to child  : //tagname[@attribute = 'value']/tagname
driver.find_element(By.XPATH,"//label[@for='bmw']/input").click()
time.sleep(2)


#parents to last child  : //tagname[@attribute = 'value']/tagname[last()]
driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']/option[last()]").click()
time.sleep(2)




#Garandparents to child  : //tagname[@attribute = 'value']/tagname/tagname
texts = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[5]/td[2]").text
print(texts,"@@@@@@@@@@")
time.sleep(2)




