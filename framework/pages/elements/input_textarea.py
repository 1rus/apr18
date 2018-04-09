from framework.pages.elements.element import Element


class Input(Element):

    def __init__(self,driver,  locator):
        self.driver = driver
        self.locator = locator

    def __set__(self, value):
        e = self.driver.find_element_by_locator(self.locator)
        e.clear()
        e.send_keys(value)

    def __get__(self, owner=None):
        e = self.driver.find_element_by_locator(self.locator)
        if e.tag_name in ["input", "textarea"]:
            return e.get_attribute("value")
        return e.text
