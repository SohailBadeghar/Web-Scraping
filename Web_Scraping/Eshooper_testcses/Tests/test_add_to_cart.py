import sys
sys.path.append('/home/neosoft/Desktop/Web-Scraping/Web_Scraping/Eshooper_testcses')
from Pages.AddToCartPage import AddToCartPage
from Base.base import EshopperBaseClass
from selenium.webdriver.common.by import By
import pytest
import time


pytest.mark.usefixtures('set_up')
class TestAddToCart(EshopperBaseClass):

    def test_addtocart_success(self):
        driver = self.driver
        self.search_product()
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//h2[normalize-space()='$500.0']").is_displayed
        assert self.driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div/div/div[1]/div/p").text == "realme Watch 2"
        assert self.driver.find_element(By.XPATH,"//a[@class='btn btn-default add-to-cart']").is_enabled
        time.sleep(5)
        Add_product = AddToCartPage(driver)
        Add_product.add_to_cart()
        Add_product.show_cart()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH,"//a[@class='btn btn-default check_out']").is_displayed
        assert self.driver.find_element(By.XPATH,"//a[@class='btn btn-default update remove-cart']").is_enabled
        assert self.driver.find_element(By.XPATH,"//img[@src='/media/product/watch_SFILZwr.webp']").is_displayed