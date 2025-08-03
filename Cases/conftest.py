import pytest
from selenium import webdriver
from utilities import ReadConfigurations


@pytest.fixture()
def setup_teardown(request):
    browser1 = ReadConfigurations.read_configuration("INFO", "browser")
    # driver = None
    if str.lower(browser1) == str.lower("chrome"):
        driver = webdriver.Chrome()
    elif str.lower(browser1) == str.lower("edge"):
        driver = webdriver.Edge()
    elif str.lower(browser1) == str.lower("firefox"):
        driver = webdriver.Firefox()
    else:
        print("provide driver from Chrome/Edge/Firefox : running default in Edge")
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(ReadConfigurations.read_configuration("INFO", "link"))
    request.cls.driver = driver
    yield
    driver.quit()
