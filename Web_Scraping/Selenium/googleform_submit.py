# Import Module


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
services=Service('chromedriver.exe')
driver = webdriver.Chrome(service=services)
# Open URL
driver.get('https://forms.gle/vWVmojtWdfFvEj8V6')

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
datas = [
	['Sohail Badeghar', 'sohailbadeghar@gmail.com', '9834000080',
		'2988 vidi gahrkul,solapur', 'NA'],
	['Arsalan', 'ArsalanKhan@gmail.com',
		'8956156159', '2143 prydarshani nagar , solapur', 'NA'],
]

# Iterate through each data
for data in datas:
	# Initialize count is zero
	count = 0

	# contain input boxes
	textboxes = driver.find_elements(By.CLASS_NAME,
		"quantumWizTextinputPaperinputInput")

	# contain textareas
	textareaboxes = driver.find_elements(By.CLASS_NAME,
		"quantumWizTextinputPapertextareaInput")

	# Iterate through all input boxes
	for value in textboxes:
		# enter value
		value.send_keys(data[count])
		# increment count value
		count += 1

	# Iterate through all textareas
	for value in textareaboxes:
		# enter value
		value.send_keys(data[count])
		# increment count value
		count += 1

	# click on submit button
	submit = driver.find_elements(By.XPATH,"//div[@class='uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd M9Bg4d']//span[@class='l4V7wb Fxmcue']").click()

	# fill another response
	another_response = driver.find_element_by_xpath(
		'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
	another_response.click()

# close the window
driver.close()
