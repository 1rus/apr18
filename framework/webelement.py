from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
from framework.exceptions import InvalidLocatorString


class WebElement(SeleniumWebElement):
    def __init__(self, element):
        self.__dict__.update(element.__dict__)

    def find_element_by_locator(self, locator):
        locator_type = locator[:locator.find('=')]
        if locator_type == "":
            raise InvalidLocatorString(locator)
        locator_value = locator[locator.find('=')+1:]
        if locator_type == "id":
            return WebElement(self.find_element_by_id(locator_value))
        elif locator_type == 'class':
            return WebElement(self.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            return WebElement(self.find_element_by_css_selector(locator_value))
        elif locator_type == 'xpath':
            return WebElement(self.find_element_by_xpath(locator_value))
        else:
            raise InvalidLocatorString(locator)

    def find_elements_by_locator(self, locator):
        locator_type = locator[:locator.find('=')]
        if locator_type == "":
            raise InvalidLocatorString(locator)
        locator_value = locator[locator.find('=')+1:]
        if locator_type == 'id':
            elements = self.find_elements_by_id(locator_value)
        elif locator_type == 'class':
            elements = self.find_elements_by_class_name(locator_value)
        elif locator_type == 'css':
            elements = self.find_elements_by_css_selector(locator_value)
        elif locator_type == 'xpath':
            elements = self.find_elements_by_xpath(locator_value)
        else:
            raise InvalidLocatorString(locator)
        return (WebElement(e) for e in elements)

