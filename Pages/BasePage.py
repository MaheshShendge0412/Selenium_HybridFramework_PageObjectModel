from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_the_element(self,locator_name,locator_value):
        element = None
        if locator_name.__contains__("_XPATH"):
            element = self.driver.find_element(By.XPATH, locator_value)
        if locator_name.__contains__("_ID"):
            element = self.driver.find_element(By.ID, locator_value)
        if locator_name.__contains__("_CLASSNAME"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        if locator_name.__contains__("CSSSELECTOR"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        if locator_name.__contains__("_NAME"):
            element = self.driver.find_element(By.NAME, locator_value)
        if locator_name.__contains__("_LINKTEXT"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        return element

    def type_into_element(self, text, locator_name,locator_value):
        element = self.get_the_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name,locator_value):
        element = self.get_the_element(locator_name,locator_value)
        element.click()
