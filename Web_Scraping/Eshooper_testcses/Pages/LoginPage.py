from Locators.locators import EshopperLocators
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.Email_inp_username = EshopperLocators.Email_inp_username
        self.Pass_inp_password = EshopperLocators.Pass_inp_password
        self.Login_submit_click = EshopperLocators.Login_submit_click
        self.Login_btn_click = EshopperLocators.Login_btn_click

    def click_to_login(self):
        self.driver.find_element(By.XPATH, self.Login_btn_click).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.Email_inp_username).clear()
        self.driver.find_element(
            By.XPATH, self.Email_inp_username).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.Pass_inp_password).clear()
        self.driver.find_element(
            By.XPATH, self.Pass_inp_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.Login_submit_click).click()
