import sys
sys.path.append('/home/neosoft/Desktop/Web-Scraping/Web_Scraping/Eshooper_testcses')
from Pages.CheckoutPage import ProductCheckoutPage
from Base.base import EshopperBaseClass
from selenium.webdriver.common.by import By
import pytest
import time


pytest.mark.usefixtures('set_up')
class TestCheckout(EshopperBaseClass):

    def test_checkout_success(self):
        driver = self.driver
        self.Add_to_cart()
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//a[@class='btn btn-default check_out']").is_displayed
        assert self.driver.find_element(By.XPATH,"//a[@class='btn btn-default update remove-cart']").is_enabled
        assert self.driver.find_element(By.XPATH,"//img[@src='/media/product/watch_SFILZwr.webp']").is_displayed
        checkout_product = ProductCheckoutPage(driver)
        checkout_product.click_to_checkout_product()
        checkout_product.select_city()
        checkout_product.select_state()
        checkout_product.select_billing_city()
        checkout_product.select_billing_state()
        checkout_product.zipcode_inp_field("417005")
        checkout_product.select_same_address()
        checkout_product.select_payment_method()
        checkout_product.continue_checkout_btn()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, "//h2[normalize-space()='Order Placed !!!']").is_displayed
        assert self.driver.find_element(By.XPATH, "//a[normalize-space()='Shop Again']").is_enabled
        assert self.driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div[1]/div/div[2]/div/div/div/ul/div/ul/li[4]/a/span").text == "0"