from Locators.locators import EshopperLocators
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time



class UserProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.Account_hover_click = EshopperLocators.Account_hover_click
        self.Profile_click = EshopperLocators.Profile_click
        self.Manage_address_click = EshopperLocators.Manage_address_click
        self.Mobile_input_field = EshopperLocators.Mobile_input_field
        self.Country_input_field = EshopperLocators.Country_input_field
        self.state_input_field = EshopperLocators.state_input_field
        self.city_input_field = EshopperLocators.city_input_field
        self.Address1_input_field = EshopperLocators.Address1_input_field
        self.Address2_input_field = EshopperLocators.Address2_input_field
        self.zipcode_input_field = EshopperLocators.zipcode_input_field
        self.saveprofile_btn = EshopperLocators.saveprofile_btn
        self.Set_default_address = EshopperLocators.Set_default_address


    def profile_click(self):
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.Account_hover_click)).perform()
        action.move_to_element(self.driver.find_element(By.XPATH, self.Profile_click)).click().perform()
        time.sleep(3)

    def mobile_no_field(self,mobile_number):
        self.driver.find_element(By.XPATH, self.Mobile_input_field).send_keys(mobile_number)

    def country_field(self,country):
        self.driver.find_element(By.XPATH,self.Country_input_field ).send_keys(country)

    def state_field(self,state):
        self.driver.find_element(By.XPATH, self.state_input_field).send_keys(state)
    
    def city_field(self,city):
        self.driver.find_element(By.XPATH, self.city_input_field).send_keys(city)

    def address1_field(self,address1):
        self.driver.find_element(By.XPATH, self.Address1_input_field).send_keys(address1)

    def address2_field(self,address2):
        self.driver.find_element(By.XPATH, self.Address2_input_field).send_keys(address2)

    def zipcode_field(self,zipcode):
        self.driver.find_element(By.XPATH, self.zipcode_input_field).send_keys(zipcode)

    def save_profile(self):
        self.driver.find_element(By.XPATH, self.saveprofile_btn).click()

    
    def set_default_address(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.Account_hover_click)).perform()
        action.move_to_element(self.driver.find_element(By.XPATH, self.Manage_address_click)).click().perform()
        self.driver.find_element(By.XPATH, self.Set_default_address).click()
