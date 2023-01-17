import sys
sys.path.append('/home/neosoft/Desktop/Web-Scraping/Web_Scraping/Eshooper_testcses')
from Pages.UserprofilePage import UserProfilePage
from Base.base import EshopperBaseClass
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.mark.usefixtures('set_up')
class TestUserProfile(EshopperBaseClass):

    def test_createprofile_success(self):
        driver = self.driver
        self.login(driver)
        time.sleep(5)
        create_profile = UserProfilePage(driver)
        create_profile.profile_click()
        assert self.driver.find_element(By.XPATH, "//b[normalize-space()='PROFILE']").is_displayed
        create_profile.mobile_no_field("9834000080")
        create_profile.country_field("India")
        create_profile.state_field("Maharashtra")
        create_profile.city_field("Pune")
        create_profile.address1_field("Blue-orchid pg,hinjewadi phase1,Pune")
        create_profile.address2_field("Blue-orchid pg,hinjewadi phase1,Pune")
        create_profile.zipcode_field("413005")
        create_profile.save_profile()
        assert self.driver.find_element(By.XPATH, "//h2[@class='title text-center']").is_displayed
        time.sleep(5)
        create_profile.set_default_address()
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//h1[@class='h4']").is_enabled

