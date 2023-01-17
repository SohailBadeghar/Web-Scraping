import sys
sys.path.append('/home/neosoft/Desktop/Web-Scraping/Web_Scraping/Eshooper_testcses')
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage 
from Base.base import EshopperBaseClass
import pytest
import time

@pytest.mark.usefixtures('set_up')
class TestLogin(EshopperBaseClass):

    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        login.click_to_login()
        login.enter_email("saifkhan@gmail.com")
        login.enter_password("admin@24")
        login.click_login()
        time.sleep(3)
        assert "Home | E-Shopper" == driver.title
        assert driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div[1]/div/div[2]/div/div/div/ul/div/ul/li[1]/a[1]").text == "Accounts"
        assert driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div[1]/div/div[2]/div/div/div/ul/div/ul/li[5]/a[1]").text == "Logout"
    
    def test_login_failure(self):
        driver = self.driver
        login = LoginPage(driver)
        login.click_to_login()
        login.enter_email("saifkhan@gmail.com")
        login.enter_password("admin")
        login.click_login()
        time.sleep(3)
        assert "Home | E-Shopper" == driver.title
        assert driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div[1]/div/div[2]/div/div/div/ul/div/ul/li[1]/a[1]").text == "Accounts"
        assert driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div[1]/div/div[2]/div/div/div/ul/div/ul/li[5]/a[1]").text == "Logout"
    