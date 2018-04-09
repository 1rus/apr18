from framework.base.base_page import BasePage

locators = {'username': 'id=txtUsername',
            'password': 'id=txtPassword',
            'submit': 'id=btnLogin',
            'err_mess': 'id=spanMessage',
            'footer': 'id=footer'
            }

base_url = 'http://hrm.seleniumminutes.com'
page_url = "/login"


class LoginPage(BasePage):

    def open(self):
        self.driver.get(base_url+page_url)

    def type_username(self, username):
        e = self.driver.find_element_by_locator(locators['username'])
        e.clear()
        e.send_keys(username)

    def type_password(self, password):
        e = self.driver.find_element_by_locator(locators['password'])
        e.clear()
        e.send_keys(password)

    def press_login(self):
        e = self.driver.find_element_by_locator(locators['submit'])
        e.click()

    def login_with(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.press_login()
        self.wait_for_available(locators['footer'])

    def get_error_message(self):
        return self.driver.find_element_by_locator(locators['err_mess']).text

