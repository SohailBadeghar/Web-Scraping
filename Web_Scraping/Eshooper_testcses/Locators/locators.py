class EshopperLocators:

    '''New User Registration '''
    Register_link = "//*[@id='form']/div/div/div/div/form/a[2]/span"
    First_name = "//input[@id='id_first_name']"
    Last_name = "//input[@id='id_last_name']"
    Eamil_address = "//input[@id='id_email']"
    Password = "//input[@id='id_password']"
    Sign_up_btn = "//button[@type='submit']"

    '''Login Locators'''
    Login_btn_click = "//a[normalize-space()='Login']"
    Email_inp_username = "//input[@id='id_username']"
    Pass_inp_password = "//input[@id='id_password']"
    Login_submit_click = "//button[@type='submit']"
    Logout_btn_css = "a[href='/accounts/user_logout/']"  # css selector

    '''UserProfile Setup'''
    Account_hover_click = "//a[normalize-space()='Accounts']"
    Profile_click = "//a[normalize-space()='Profile']"
    Manage_address_click = "//ul[@role='menu']//a[normalize-space()='Manage Adresses']"
    Mobile_input_field = "//input[@id='id_mobile_number']"
    Country_input_field = "//input[@id='id_country']"
    state_input_field = "//input[@id='id_state']"
    city_input_field = "//input[@id='id_city']"
    Address1_input_field = "//input[@id='id_address_1']"
    Address2_input_field = "//input[@id='id_address_2']"
    zipcode_input_field = "//input[@id='id_zipcode']"
    saveprofile_btn = "//button[@type='submit']"
    Set_default_address = "//a[normalize-space()='Set Default']"

    '''Search Product'''
    search_bar_field = "//input[@placeholder='Search']"
    add_to_cart_btn = "//a[@class='btn btn-default add-to-cart']"
    price_of_product = "//h2[normalize-space()='$500.0']"
    product_name = "/html/body/section[2]/div/div/div[2]/div/div/div/div[1]/div/p"

    ''' Add to cart Product'''
    cart_btn = "//a[contains(.,'Cart 1')]"

    '''Add to wishlist'''
    

    '''Checkout Process of product'''
    checkout_product_btn = "//a[@class='btn btn-default check_out']"
    check_box_click_same_address_fill = "//input[@id='same-address']"
    city_drop_field = " //select[@id='id_shipping_city']"
    state_drop_field = " //select[@id='id_shipping_state']"
    billing_city_drop_field = "//select[@id='id_billing_city']"
    billing_state_drop_field = "//select[@id='id_billing_state']"
    zipcode_input_field = "//input[@id='bill_zip']"
    cod_payment_option = "//label[@for='COD']"
    continue_checkout = "//button[@type='submit']"
    