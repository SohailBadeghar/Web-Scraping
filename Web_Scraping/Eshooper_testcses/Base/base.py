import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.ProductSearchPage import ProductSearchPage
from Pages.AddToCartPage import AddToCartPage
import time


class EshopperBaseClass:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://neoeshopper.pythonanywhere.com/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()

    def login_before_signup(self, driver):
        driver = self.driver
        login = LoginPage(driver)
        login.click_to_login()

    def login(self, driver):
        driver = self.driver
        login = LoginPage(driver)
        login.click_to_login()
        login.enter_email("saifkhan@gmail.com")
        login.enter_password("admin@24")
        login.click_login()

    def search_product(self):
        driver = self.driver
        self.login(driver)
        time.sleep(5)
        search_product = ProductSearchPage(driver)
        search_product.search_products("realme Watch 2")
        search_product.search_submit_name()
        time.sleep(3)

    def Add_to_cart(self):
        driver = self.driver
        self.search_product()
        time.sleep(5)
        Add_product = AddToCartPage(driver)
        Add_product.add_to_cart()
        Add_product.show_cart()
        time.sleep(3)
