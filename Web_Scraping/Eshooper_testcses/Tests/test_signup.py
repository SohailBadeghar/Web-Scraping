import sys
sys.path.append('/home/neosoft/Desktop/Web-Scraping/Web_Scraping/Eshooper_testcses')
from Pages.RegistrationPage import RegistrationPage 
from Base.base import EshopperBaseClass
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.mark.usefixtures('set_up')
class TestSignup(EshopperBaseClass):

    def test_signup_success(self):
        driver = self.driver
        self.login_before_signup(driver)
        time.sleep(5)
        signup = RegistrationPage(driver)
        signup.create_new_user_link()
        signup.firstname_input("samkaran")
        signup.lastname_input("shinde")
        signup.email_input("sam@gmail.com")
        signup.password_input("admin@24")
        signup.signupfrom_submit()
        time.sleep(7)
        assert driver.find_element(By.XPATH,"//div[@class='col-sm-4 col-sm-offset-4']/div/h2").text == "Login to your account"
        assert driver.find_element(By.XPATH, "//a[normalize-space()='Login']").is_displayed
        assert "Home | E-Shopper" == driver.title

        

    def test_signup_failure(self):
        driver = self.driver
        self.login_before_signup(driver)
        signup = RegistrationPage(driver)
        signup.create_new_user_link()
        signup.firstname_input("samkaran")
        signup.lastname_input("shinde")
        signup.email_input("sam@gmail.com")
        signup.password_input("admin@24")
        signup.signupfrom_submit()
        time.sleep(2)
        assert driver.find_element(By.XPATH,"//div[@class='col-sm-4 col-sm-offset-4']/div/h2").text == "Login to your account"
        assert driver.find_element(By.XPATH, "//a[normalize-space()='Login']").is_displayed
        assert "Home | E-Shopper" == driver.title
