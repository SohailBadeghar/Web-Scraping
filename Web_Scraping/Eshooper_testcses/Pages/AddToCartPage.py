from Locators.locators import EshopperLocators
from selenium.webdriver.common.by import By



class AddToCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = EshopperLocators.add_to_cart_btn
        self.cart_btn = EshopperLocators.cart_btn


    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_btn).click()

    def show_cart(self):
        self.driver.find_element(By.XPATH, self.cart_btn).click()
