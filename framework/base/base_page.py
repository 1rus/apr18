import os
import os.path
import time
from framework.exceptions import ElementTextTimeout, ElementVisiblityTimeout
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

class BasePage (object):

    timeout_seconds = 30
    sleep_interval = .25
    short_sleep = .002

    def __init__(self, driver):
        self.driver = driver

    def sleep(self, seconds=None):
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(self.sleep_interval)

    def is_element_available(self, locator):
        if self.driver.is_element_present(locator):
            if self.driver.is_visible(locator):
                return True
            else:
                return False
        else:
            return False

    def wait_for_available(self, locator):
        for i in range(self.timeout_seconds):
            try:
                if self.driver.is_element_available(locator):
                    break
            except:
                pass
            self.sleep()
        else:
            raise ElementVisiblityTimeout('%s availability timed out' % locator)
        return True

    def wait_for_visible(self, locator):
        for i in range(self.timeout_seconds):
            try:
                if self.driver.is_visible(locator):
                    break
            except:
                pass
            self.sleep()
        else:
            raise ElementVisiblityTimeout("%s visibility timed out" % locator)
        return True

    def wait_for_hidden(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_visible(locator):
                time.sleep()
            else:
                break
        else:
            raise ElementVisiblityTimeout("%s visibility timed out" % locator)
        return True

    def wait_for_text(self, locator, text):
        for i in range(self.timeout_seconds):
            try:
                e = self.driver.find_element_by_locator(locator)
                if e.text == text:
                    break
            except:
                pass
            self.sleep()
        else:
            raise ElementTextTimeout("%s value timed out" % locator)
        return True

    def wait_for_value(self, locator, text):
        for i in range(self.timeout_seconds):
            try:
                e = self.driver.find_element_by_locator(locator)
                if e.value == text:
                    break
            except:
                pass
            self.sleep()
        else:
            raise ElementTextTimeout("%s value timed out" % locator)
        return True

    def wait_for_value_change(self, locator, text):
        e = self.driver.find_element_by_locator(locator)
        for i in range(self.timeout_seconds):
            try:
                if len(e.text.strip()) != 0 and e.text != text:
                    return True
            except StaleElementReferenceException:
                e = self.driver.find_element_by_locator(locator)
            finally:
                self.sleep()
        else:
            raise ElementVisiblityTimeout("%s change value exception" % locator)

    def title(self):
        return self.driver.title

