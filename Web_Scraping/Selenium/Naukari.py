import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


driver.get("https://www.naukri.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@class='suggestor-input ']").send_keys("Python Django Developer")

static_dropdown = driver.find_element(By.XPATH," //span[@class='dropArrowDD']").click()
dropdown = driver.find_element(By.XPATH,"//*[@id='root']/div[6]/div/div/div[3]/div/div/div")
dropdown.find_element(By.CSS_SELECTOR,"li[value='#1']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter location']").send_keys("Pune")
driver.find_element(By.XPATH,"//div[@class='qsbSubmit']").click()
time.sleep(5)
Job_details = driver.find_elements(By.CLASS_NAME,"jobTuple")
print(Job_details,"@@@@@@@@@@@")
for job in Job_details:
    job_role = job.find_element(By.XPATH,"//body/div[@id='root']/div[@class='search-result-container']/div[@class='search-result-wrap']/div[@class='content']/section[@class='listContainer fleft']/div[@class='list']/article[1]/div[1]/div[1]/a[1]").text
    company_name = job.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/section[2]/div[2]/article[1]/div[1]/div[1]/div/a").text
    year_of_experience_required = job.find_element(By.XPATH,"//article[1]//div[1]//ul[1]//li[1]").text

