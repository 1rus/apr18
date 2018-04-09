from framework.pages.elements.element import Element


class CheckBox(Element):

        def __init__(self, driver, locator):
            self.driver = driver
            self.locator = locator

        def __set__(self, value):
            e = self.driver.find_element_by_locator(self.locator)
            current = e.is_selected()
            if current != value:
                e.click()

        def __get__(self):
            e = self.driver.find_element_by_locator(self.locator)
            return e.is_selected()
