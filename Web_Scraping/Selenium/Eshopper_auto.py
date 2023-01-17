import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class SeleniumDriver:
    def __init__(self):
        services = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=services)

    '''
    Entry point of website open.
    '''

    def login_entry(self):
        self.driver.get("https://neoeshopper.pythonanywhere.com/")
        self.driver.maximize_window()
        time.sleep(3)

    '''
    Process to Register new User.
    '''

    def register_new_user(self):
        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(
            By.XPATH, "//span[normalize-space()='Create Your New Account ?']").click()
        self.driver.find_element(
            By.XPATH, "//input[@id='id_first_name']").send_keys("Saif")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_last_name']").send_keys("Khan")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_email']").send_keys("saifkhan@gmail.com")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_password']").send_keys("admin@24")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    '''
    Redirect to the login page.
    '''

    def redirect_login_page(self):
        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Log In']").click()

    '''
    User login to the Ecommerce website.via .login page.
    '''

    def login_into_website(self):
        self.driver.find_element(
            By.XPATH, "//input[@id='id_username']").send_keys("saifkhan@gmail.com")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_password']").send_keys("admin@24")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    '''
    Setup the profile details of User.
    '''

    def redirect_to_profile(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Accounts']")).perform()
        action.move_to_element(self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Profile']")).click().perform()

    '''
    Fill the profile form.
    '''

    def profile_form_filling(self):
        self.driver.find_element(
            By.XPATH, "//input[@id='id_mobile_number']").send_keys("9834000080")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_country']").send_keys("India")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_state']").send_keys("Maharashtra")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_city']").send_keys("Pune")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_address_1']").send_keys("Blue-orchid pg,hinjewadi phase1,Pune")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_address_2']").send_keys("Blue-orchid pg,hinjewadi phase1,Pune")
        self.driver.find_element(
            By.XPATH, "//input[@id='id_zipcode']").send_keys("417005")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    '''
    for setting default address go to manage address.
    '''

    def set_default_address(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Accounts']")).perform()
        action.move_to_element(self.driver.find_element(
            By.XPATH, "//ul[@role='menu']//a[normalize-space()='Manage Adresses']")).click().perform()

        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Set Default']").click()
    '''
    After login in home page search the product and get that product.
    '''

    def search_product(self):
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Search']").send_keys("realme Watch 2")
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Search']").submit()
        time.sleep(5)

    '''
    After Getting the product it will add to the cart
    '''

    def add_to_cart(self):
        self.driver.find_element(
            By.XPATH, "//a[@class='btn btn-default add-to-cart']").click()
        self.driver.find_element(By.XPATH, "//a[contains(.,'Cart 1')]").click()

    '''
    Product Checkout procedure.
    '''
    def product_checkout(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']").click()

        static_dropdown = Select(self.driver.find_element(By.XPATH," //select[@id='id_shipping_city']"))
        static_dropdown.select_by_value("Pune")

        static_dropdown = Select(self.driver.find_element(By.XPATH," //select[@id='id_shipping_state']"))
        static_dropdown.select_by_value("Maharashtra")

        static_dropdown = Select(self.driver.find_element(By.XPATH," //select[@id='id_billing_city']"))
        static_dropdown.select_by_value("Pune")

        static_dropdown = Select(self.driver.find_element(By.XPATH," //select[@id='id_billing_state']"))
        static_dropdown.select_by_value("Maharashtra")

        self.driver.find_element(By.XPATH,"//input[@id='bill_zip']").send_keys("417005")
        self.driver.find_element(By.XPATH,"//input[@id='same-address']").click()


        self.driver.find_element(By.XPATH,"//label[@for='COD']").click()
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

        time.sleep(5)

eshopper_driver = SeleniumDriver()
eshopper_driver.login_entry()
eshopper_driver.register_new_user()
eshopper_driver.redirect_login_page()
eshopper_driver.login_into_website()
eshopper_driver.redirect_to_profile()
eshopper_driver.profile_form_filling()
eshopper_driver.set_default_address()
eshopper_driver.search_product()
eshopper_driver.add_to_cart()
eshopper_driver.product_checkout()