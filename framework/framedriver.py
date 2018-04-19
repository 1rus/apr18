from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from framework.exceptions import InvalidLocatorString
from framework.webelement import WebElement
import framework.exceptions


class FrameWebdriver(webdriver.Remote):

    def __init__(self, **kwargs):
        super(FrameWebdriver, self).__init__(**kwargs)

    def find_element_by_locator(self, locator):
        locator_type = locator[:locator.find('=')]
        if locator_type == '':
            raise framework.exceptions.InvalidLocatorString(locator)
        locator_value = locator[locator.find('=')+1:]
        if locator_type == 'id':
            return self.find_element_by_id(locator_value)
        elif locator_type == 'class':
            e = WebElement(self.find_element_by_class_name(locator_value))
        elif locator_type == 'tag':
            e = WebElement(self.find_element_by_tag_name(locator_value))
        elif locator_type == 'css':
            e = WebElement(self.find_element_by_css_selector(locator_value))
        elif locator_type == 'xpath':
            e = WebElement(self.find_element_by_xpath(locator_value))
        else:
            raise InvalidLocatorString(locator)
        return e


    def find_elements_by_locator(self, locator):
        locator_type = locator[:locator.find('=')]
        if locator_type == '':
            raise framework.exceptions.InvalidLocatorString(locator)
        locator_value = locator[locator.find('=')+1:]
        if locator_type == 'id':
            elements = self.find_elements_by_id(locator_value)
        elif locator_type == 'class':
            elements = self.find_elements_by_class_name(locator_value)
        elif locator_type == 'tag':
            elements = self.find_elements_by_tag_name(locator_value)
        elif locator_type == 'css':
            elements = self.find_elements_by_css_selector(locator_value)
        elif locator_type == 'xpath':
            elements = self.find_elements_by_xpath(locator_value)
        else:
            raise InvalidLocatorString(locator)
        return [WebElement(e) for e in elements]

    def is_element_present(self, locator):
        try:
            self.find_element_by_locator(locator)
            return True
        except NoSuchElementException:
            return False

    def is_visible(self, locator):
        if self.is_element_present(locator):
            if self.find_element_by_locator(locator).is_displayed():
                return True
            else:
                return False
        else:
            return False

    def is_element_available(self, locator):
        if self.is_visible(locator):
            return True
        else:
            return False

