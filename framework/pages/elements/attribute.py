from framework.pages.elements.element import Element


class Attribute(Element):

    def __init__(self, locator, attribute):
        self.locator = locator
        self.attribute = attribute

    def __set__(self, driver, value):
        pass

    def __get__(self, driver):
        try:
            e = driver.find_element_by_locator(self.locator)
            v = e.get_attribute(self.attribute)
            return v
        except AttributeError:
            pass
