from Locators.locators import EshopperLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class ProductCheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_product_btn = EshopperLocators.checkout_product_btn
        self.check_box_click_same_address_fill = EshopperLocators.check_box_click_same_address_fill
        self.city_drop_field = EshopperLocators.city_drop_field
        self.state_drop_field = EshopperLocators.state_drop_field
        self.billing_city_drop_field = EshopperLocators.billing_city_drop_field
        self.billing_state_drop_field = EshopperLocators.billing_state_drop_field
        self.zipcode_input_field = EshopperLocators.zipcode_input_field
        self.cod_payment_option = EshopperLocators.cod_payment_option
        self.continue_checkout = EshopperLocators.continue_checkout


    def click_to_checkout_product(self):
        self.driver.find_element(By.XPATH, self.checkout_product_btn ).click()

    def select_city(self):
        static_dropdown = Select(self.driver.find_element(By.XPATH, self.city_drop_field))
        static_dropdown.select_by_value("Pune")

    def select_state(self):
        static_dropdown = Select(self.driver.find_element(By.XPATH,self.state_drop_field ))
        static_dropdown.select_by_value("Maharashtra")

    def select_billing_city(self):
        static_dropdown = Select(self.driver.find_element(By.XPATH, self.billing_city_drop_field))
        static_dropdown.select_by_value("Pune")
    
    def select_billing_state(self):
        static_dropdown = Select(self.driver.find_element(By.XPATH,self.billing_state_drop_field ))
        static_dropdown.select_by_value("Maharashtra")

    def zipcode_inp_field(self, zipcode):
        self.driver.find_element(By.XPATH, self.zipcode_input_field).send_keys(zipcode)

    def select_same_address(self):
        self.driver.find_element(By.XPATH, self.check_box_click_same_address_fill).click()

    def select_payment_method(self):
        self.driver.find_element(By.XPATH, self.cod_payment_option).click()

    def continue_checkout_btn(self):
        self.driver.find_element(By.XPATH,self.continue_checkout).click()



