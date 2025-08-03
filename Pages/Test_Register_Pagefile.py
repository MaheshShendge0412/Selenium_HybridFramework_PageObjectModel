import pytest
from Pages.BasePage import BasePage


# All the locator's required for test_register.py file are here

class Test_Register_Page(BasePage):
    # constructor
    def __init__(self, driver):
        super().__init__(driver)  # pointing to base class in BasePage.py

    register_FirstNameLocator_ID = "firstname"
    register_lastname_Locator_ID = "lastname"
    register_username_Locator_ID = "username"
    register_password_Locator_ID = "password"
    register_button_Locator_XPATH = "//input[@value='Register']"
    register_button_locator_CSSSELECTOR = "input[value='Register']"

    def enter_Register_button(self):
        self.element_click("register_button_locator_CSSSELECTOR", self.register_button_locator_CSSSELECTOR)

    def enter_name_into_name_field(self, namevalue):
        self.type_into_element(namevalue, "register_FirstNameLocator_ID", self.register_FirstNameLocator_ID)

    def enter_last_name_into_last_name_field(self, lastnamevalue):
        self.type_into_element(lastnamevalue, "register_lastname_Locator_ID", self.register_lastname_Locator_ID)

    # @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel("ExcelFiles/DataDrivenTesting.xlsx", "credentials"))
    def enter_username_into_username(self, usenameValue):
        self.type_into_element(usenameValue, "register_username_Locator_ID", self.register_username_Locator_ID)

    def enter_password_into_password(self, passwordValue):
        self.type_into_element(passwordValue, "register_password_Locator_ID", self.register_password_Locator_ID)
