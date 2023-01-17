import sys
sys.path.append('/home/neosoft/Desktop/Web-Scraping/Web_Scraping/Eshooper_testcses')
from Pages.ProductSearchPage import ProductSearchPage
from Base.base import EshopperBaseClass
from selenium.webdriver.common.by import By
import pytest
import time


pytest.mark.usefixtures('set_up')
class TestLogin(EshopperBaseClass):

    def test_search_success(self):
        driver = self.driver
        self.login(driver)
        time.sleep(5)
        search_product = ProductSearchPage(driver)
        search_product.search_products("realme Watch 2")
        search_product.search_submit_name()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH,"//h2[normalize-space()='$500.0']").is_displayed
        assert self.driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div/div/div[1]/div/p").text == "realme Watch 2"
        assert self.driver.find_element(By.XPATH,"//a[@class='btn btn-default add-to-cart']").is_enabled
        assert "Home | E-Shopper" == driver.title