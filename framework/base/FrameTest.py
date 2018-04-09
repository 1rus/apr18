from framework.browser import Browser
import os.path
from framework.base.BaseTest import BaseTestCase
from framework.wrapconfig import Config
from framework.assertions import Assertions
import pytest


class FrameTestCase(BaseTestCase):

    @classmethod
    def setup_class(self):
        c = Config()
        self.config = c.prepare()
        browser_conf = self.config["browser"]
        self.browser = Browser(browser_conf, self.config)
        self._screenshot_number = 1
        self.verification_errors = []
        self.driver = self.browser.driver
        self.assertions = Assertions(self.driver, self.verification_errors)

    @classmethod
    def teardown_class(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def setup_method(self, method):
        self.current_method = method.__name__


    def take_numbered_screenshot(self):
        if self.config["sframe"]["screenshots"]:
            output_dir = self.prepare_screenshots_dir()
            self.driver.get_screenshot_as_file(os.path.join(output_dir, str(self._screenshot_number).zfill(3)+".png"))
            self._screenshot_number = self._screenshot_number+1

    def take_named_screenshot(self, name):
        method_dir = self.prepare_screenshots_dir()
        image_path = os.path.join(method_dir, str(name) + ".png")
        self.driver.get_screenshot_as_file(image_path) 