# to optimise fixture this code is written
# Creating BaseTest class as a parent class and adding that as a parent in every test cases class
import pytest


@pytest.mark.usefixtures("setup_teardown")
class BaseTest:
    pass
