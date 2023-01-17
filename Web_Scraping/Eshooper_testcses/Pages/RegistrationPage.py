from Locators.locators import EshopperLocators
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class RegistrationPage:
    

    def __init__(self, driver):
        self.driver = driver
        self.Register_link = EshopperLocators.Register_link
        self.First_name = EshopperLocators.First_name
        self.Last_name = EshopperLocators.Last_name
        self.Eamil_address = EshopperLocators.Eamil_address
        self.Password = EshopperLocators.Password
        self.Sign_up_btn = EshopperLocators.Sign_up_btn


    def create_new_user_link(self):
        time.sleep(2)
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.Register_link)
        action.move_to_element(element).click().perform()

    def firstname_input(self, first_name,):
        self.driver.find_element(By.XPATH, self.First_name).send_keys(first_name)

    def lastname_input(self, last_name):
        self.driver.find_element(By.XPATH, self.Last_name).send_keys(last_name)

    def email_input(self, email):
        self.driver.find_element(By.XPATH, self.Eamil_address).send_keys(email)

    def password_input(self, password):
        self.driver.find_element(By.XPATH, self.Password).send_keys(password)

    def signupfrom_submit(self):
        self.driver.find_element(By.XPATH, self.Sign_up_btn).click()
