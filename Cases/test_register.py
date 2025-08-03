import time
from Cases.BaseTest import BaseTest
from Pages.Test_Register_Pagefile import Test_Register_Page
from utilities.ExcelUtils import get_cell_data


class TestRegister(BaseTest):
    def test_register(self):
        obj_Test_Register_Page_class = Test_Register_Page(self.driver)
        # data driven
        obj_Test_Register_Page_class.enter_name_into_name_field(get_cell_data("ExcelFiles/DataDrivenTesting.xlsx", "register", 2, 1))
        obj_Test_Register_Page_class.enter_last_name_into_last_name_field(get_cell_data("ExcelFiles/DataDrivenTesting.xlsx", "register", 2, 2))
        obj_Test_Register_Page_class.enter_username_into_username(get_cell_data("ExcelFiles/DataDrivenTesting.xlsx", "register", 2, 3))
        obj_Test_Register_Page_class.enter_password_into_password(get_cell_data("ExcelFiles/DataDrivenTesting.xlsx", "register", 2, 3))

        """
        obj_Test_Register_Page_class.enter_name_into_name_field("Indians")
        obj_Test_Register_Page_class.enter_last_name_into_last_name_field("Indians")
        obj_Test_Register_Page_class.enter_username_into_username("Mumbai_Indians")
        obj_Test_Register_Page_class.enter_password_into_password("MUMBAI_INDIANS2025")
        """
        time.sleep(10)
