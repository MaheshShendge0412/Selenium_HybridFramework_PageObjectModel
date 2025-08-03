import time
import pytest
from utilities import ExcelUtils
from utilities.ExcelUtils import get_data_from_excel
from Cases.BaseTest import BaseTest
from Pages.Test_Textbox import Test_Textbox_class


class TestLogin(BaseTest):
    def test_login(self):
        username_string = "Mumbai_Indians"
        password_string = "MUMBAI_INDIANS2025"
        # data driven
        data_list = get_data_from_excel("ExcelFiles/DataDrivenTesting.xlsx","credentials")

        obj_textbox = Test_Textbox_class(self.driver)
        obj_textbox.backTo_login_button_click()
        obj_textbox.enter_usernameToLogIn(data_list[0])
        time.sleep(1)
        obj_textbox.enter_PasswordToLogIn(data_list[1])
        obj_textbox.click_login()
        time.sleep(10)
