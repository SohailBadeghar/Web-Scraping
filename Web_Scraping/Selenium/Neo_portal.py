import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)

driver.get("https://emp.neosofttech.com/")
driver.maximize_window()
driver.find_element(By.ID, "loginform-email").send_keys("sohail.badeghar")
a = driver.find_element(By.XPATH,"//*[@id='login-form']/div[1]/div/select/option[3]").click()
print(a)
time.sleep(5)
# driver.get("http://connecto2.neosofttech.com/public/get-mpin")
driver.find_elements(By.LINK_TEXT,"Click here")[1].click()
a = driver.window_handles[1]
driver.switch_to.window(a)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("sohail.badeghar")
driver.find_element(By.ID,"mpin_submit").click()
time.sleep(10)

