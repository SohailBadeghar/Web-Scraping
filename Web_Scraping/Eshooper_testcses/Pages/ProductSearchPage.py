from Locators.locators import EshopperLocators
from selenium.webdriver.common.by import By



class ProductSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar_field = EshopperLocators.search_bar_field
        self.add_to_cart_btn = EshopperLocators.add_to_cart_btn
        self.price_of_product = EshopperLocators.price_of_product
        self.product_name = EshopperLocators.product_name


    def search_products(self, product_name):
        self.driver.find_element(By.XPATH, self.search_bar_field).send_keys(product_name)

    def search_submit_name(self):
        self.driver.find_element(By.XPATH,self.search_bar_field ).submit()

