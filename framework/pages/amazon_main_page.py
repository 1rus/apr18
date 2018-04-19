from framework.base.base_page import BasePage
from framework.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from framework.pages.elements.checkbox import CheckBox
from framework.pages.elements.select import Select
from decimal import *

locators = {'main_search_field': 'css=input#twotabsearchtextbox',
            'results': "#s-result-count",
            'no_results': "css=#noResultsTitle",
            'main_search_button': 'css=input.nav-input[value="Go"]',
            'search_price_go': "css=input.a-button-input[type='submit'][value='Go']",
            'left_nav_section': "css=#leftNavContainer>h3",
            'colors': "xpath=following-sibling::ul[2]/li/span/a",
            'stars': "css=ul>div>li>span>a>i[class*='star']",
            'search_titles': "css=#leftNavContainer>h4",
            'search_price_low': "css=#low-price",
            'search_price_high': "css=#high-price",
            'following_input_list': "xpath=following-sibling::*[1]/div/li/span/span/div/label/input",
            'following_sibling': "xpath=following-sibling::*[1]",
            'following_input_title': "xpath=following-sibling::*[2]/span",
            'following_option_list': "xpath=following-sibling::*[1]/div/li/span/a",
            'option_title': "xpath=.//span",
            'results_list': "css=li[id^='result_']",
            'results_title': "css=div:nth-child(1)>div:nth-child(3)>div:nth-child(1)>a>h2:nth-child(1)",
            'results_price': "css=div:nth-child(1)>div:nth-child(4)>div:nth-child(1)>a>span:nth-child(1)",
            'results_rating': "css=div>div>span>span>a>i>span",
            'sort_by': "css=select[id='sort']",
            }

base_url = 'https://www.amazon.com'
refine_search_dict = {}
price_range = [20, 100]


class MainPage(BasePage):

    def open(self):
        self.driver.get(base_url)
        self.wait_for_available(locators['main_search_field'])

    def search_amazon_for(self, search_string):
        e = self.driver.find_element_by_locator(locators['main_search_field'])
        e.clear()
        e.send_keys(search_string)
        self.driver.find_element_by_locator(locators["main_search_button"]).click()
        self.wait_for_available(locators['left_nav_section'])
        try:
            self.driver.find_element_by_locator(locators["no_results"])
            raise Exception("no results, try another search")
        except NoSuchElementException:
            pass

    def refine_search_with(self, ref, opt):
        refine_by = ref.lower()
        if "price" in refine_by and isinstance(opt, list):
            el = self.driver.find_element_by_locator(locators['search_price_low'])
            el.clear()
            el.send_keys(price_range[0])
            el = self.driver.find_element_by_locator(locators['search_price_high'])
            el.clear()
            el.send_keys(price_range[1])
            self.driver.find_element_by_locator(locators['search_price_go']).click()
        else:
            option = opt.lower()
            ref_dict = self.get_refine_search_dict()
            if refine_by in ref_dict.keys() and option in ref_dict[refine_by]:
                el = refine_search_dict[refine_by][option]
                if isinstance(el, WebElement):
                    WebElement(el).click()
                else:
                    self.driver.find_element_by_locator(el).click()
            else:
                raise Exception('No such option or refine by parameter in the dict')
        self.wait_for_available(locators['left_nav_section'])

    def get_refine_search_dict(self):
        if not refine_search_dict:
            left_nav_sections = self.driver.find_elements_by_locator(locators["left_nav_section"])
            refine_search_by_titles = self.driver.find_elements_by_locator(locators["search_titles"])
            for nav_section in left_nav_sections:
                if nav_section.text.lower() == "refine by":
                    for search_title in refine_search_by_titles:
                        title = WebElement(search_title).text.lower()
                        refine_search_dict[title] = {}
                        if "case color" in title:
                            case_colors = WebElement(search_title).find_elements_by_locator(locators["colors"])
                            for color in case_colors:
                                refine_search_dict[title][color.get_attribute("title").lower()] = color
                        elif "amazon prime" in title:
                            option = "prime"
                            name = WebElement(search_title).find_element_by_locator(locators["following_input_list"]).get_attribute("name")
                            loc = "css=input[type='checkbox'][name='" + name + "']"
                            refine_search_dict[title][option] = CheckBox(self.driver, loc)
                        elif "customer review" in title:
                            customer_stars = self.driver.find_elements_by_locator(locators["stars"])
                            for star in customer_stars:
                                option = star.get_attribute("class")
                                num_of_stars = option[option.rfind("-") + 1:]
                                refine_search_dict[title][num_of_stars + " stars & up"] = star
                        else:
                            try:
                                input_list = WebElement(search_title).find_elements_by_locator(locators["following_input_list"])
                                for input_checkbox in input_list:
                                    attr = input_checkbox.get_attribute("name")
                                    name = WebElement(input_checkbox).find_element_by_locator(locators["following_input_title"]).text.lower()
                                    loc = "css=input[type='checkbox'][name='" + attr + "']"
                                    refine_search_dict[title][name] = loc
                            except NoSuchElementException:
                                raise Exception("exception, NOT inputs ")
                            try:
                                i = 1
                                option_list = WebElement(search_title).find_elements_by_locator(locators["following_option_list"])
                                for option in option_list:
                                    i += 1
                                    name = WebElement(option).find_element_by_locator(locators["option_title"]).text.lower()
                                    link = option.get_attribute("href")
                                    loc = "css=a[href='" + link[link.find(".com") + 4:] + "']"
                                    refine_search_dict[title][name] = loc
                            except NoSuchElementException:
                                raise Exception("exception, NO lists ")
        return refine_search_dict

    def get_results(self):
        titles = []
        prices = []
        ratings = []
        els = self.driver.find_elements_by_locator(locators["results_list"])
        for el in els:
            title = WebElement(el).find_element_by_locator(locators['results_title']).text[:16]
            try:
                p = WebElement(el).find_element_by_locator(locators['results_price']).get_attribute("innerHTML")
                r = WebElement(el).find_element_by_locator(locators['results_rating']).get_attribute("innerText")
                if len(p) > 0 and len(r) > 0:
                    titles.append(title)
                    prices.append(Decimal(p[1:]))
                    ratings.append(Decimal(r[:r.find(" ")]))
            except NoSuchElementException:
                pass
        return titles, prices, ratings

    def sort_by(self, param):
        sort_by = Select(self.driver, (locators["sort_by"]))
        try:
            sort_by.__set__(param)
        except NoSuchElementException:
            raise Exception("no such sort option")
        self.wait_for_available(locators['left_nav_section'])
