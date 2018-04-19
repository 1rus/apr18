from framework.pages.elements.element import Element
from selenium.webdriver.support.select import Select as SeleniumSelect
from framework.exceptions import InvalidLocatorString
from framework.webelement import WebElement


class Select(SeleniumSelect):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def __set__(self, val):
        s = SeleniumSelect(self.driver.find_element_by_locator(self.locator))
        method = val[:val.find("=")]
        value = val[val.find("=")+1:]
        if method == "value":
            s.select_by_value(value)
        elif method == "index":
            s.select_by_index(value)
        elif method == "text":
            s.select_by_visible_text(value)
        else:
            raise InvalidLocatorString(value)

    def __get__(self):
        try:
            s = SeleniumSelect(self.driver.find_element_by_locator(self.locator))
            e = s.first_selected_option
            return str(e.text)
        except AttributeError:
            pass
