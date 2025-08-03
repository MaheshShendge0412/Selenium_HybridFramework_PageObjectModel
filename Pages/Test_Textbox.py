import pytest
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


# All the locator's required for test_textbox.py file are here

class Test_Textbox_class(BasePage):
    # constructor
    def __init__(self, driver):
        super().__init__(driver)  # pointing to base class in BasePage.py

    # locators
    textbox_login_button_locator_XPATH = "//a[normalize-space()='Back to Login']"
    textbox_enter_username_locator_XPATH = "//input[@id='email']"
    textbox_enter_password_locator_XPATH = "//input[@id='password']"
    textbox_loginClick_locator_XPATH = "//input[@value='Login']"

    # Methods working on locators
    def backTo_login_button_click(self):
        self.driver.find_element(By.XPATH, self.textbox_login_button_locator_XPATH).click()

    def click_login(self):
        self.element_click("textbox_loginClick_locator_XPATH", self.textbox_loginClick_locator_XPATH)

    def enter_usernameToLogIn(self, usernameValue):
        self.type_into_element(usernameValue, "textbox_enter_username_locator_XPATH",
                               self.textbox_enter_username_locator_XPATH)  # this function defined in BasePage.py

    def enter_PasswordToLogIn(self, passwordValue):
        self.type_into_element(passwordValue, "textbox_enter_password_locator_XPATH", self.textbox_enter_password_locator_XPATH)
