from selenium.common.exceptions import NoSuchElementException
from framework.browser import Browser
from framework.webelement import WebElement
from framework.pages.elements import checkbox
from framework.pages.elements.checkbox import CheckBox
from selenium.webdriver.chrome.options import Options
from framework.assertions import Assertions
from decimal import *
from framework.pages.elements.select import Select
from collections import namedtuple
import numpy
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap_map = {
    "firefox": DesiredCapabilities.FIREFOX.copy(),
    "internet explorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "internetexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "iexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "ie": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "chrome": DesiredCapabilities.CHROME.copy(),
    "opera": DesiredCapabilities.OPERA.copy(),
    "phantomjs": DesiredCapabilities.PHANTOMJS.copy(),
    "htmlunitjs": DesiredCapabilities.HTMLUNITWITHJS.copy(),
    "htmlunit": DesiredCapabilities.HTMLUNIT.copy(),
    "iphone": DesiredCapabilities.IPHONE.copy(),
    "ipad": DesiredCapabilities.IPAD.copy(),
    "android": DesiredCapabilities.ANDROID.copy(),
    "edge": DesiredCapabilities.EDGE.copy(),
    "safari": DesiredCapabilities.SAFARI.copy()
}

locators = {'main_search_field': 'css=input#twotabsearchtextbox',
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
refine_search_dict = {}


def get_results():
    titles = []
    prices = []
    ratings = []
    els = browser.driver.find_elements_by_locator(locators["results_list"])
    i = 1
    for el in els:
        title = WebElement(el).find_element_by_locator(locators['results_title']).text[:16]
        try:
            p = WebElement(el).find_element_by_locator(locators['results_price']).get_attribute("innerHTML")
            r = WebElement(el).find_element_by_locator(locators['results_rating']).get_attribute("innerText")
            print(title, p, r)
            if len(p) > 0 and len(r) > 0:
                titles.append(title)
                prices.append(Decimal(p[1:]))
                ratings.append(Decimal(r[:r.find(" ")]))
                print('title %s \t price %s \t rating %s' % (title, p, r))
                i += 1
        except NoSuchElementException:
            pass
    return titles, prices, ratings


def sort_by(param):
    select_sort_by = Select(browser.driver, (locators["sort_by"]))
    try:
        select_sort_by.__set__(param)
    except NoSuchElementException:
        raise ("no such sort option")


price_range = [20, 100]
caps = cap_map['chrome']
conf = {'selenium': {'timeout': 30, 'executor': {'host': '10.0.0.215', 'port': 5555, 'is grid': False}, 'proxy': {'url': '', 'type': ''}}, 'browser': {'type': 'chrome', 'profiles': {'darwin': None, 'profile': None}, 'grid filters': {'platform': 'mac', 'version': '23.0.1'}}, 'sframe': {'base': 'D:\\PROJECTS\\AMAZON', 'default_browser': 'rabbit', 'ci_type': 'jenkins', 'screenshots': {'on_failure': False, 'on_error': True, 'on_finish': False}}}
br_conf = conf["browser"]
browser = Browser(br_conf, conf)
assert_that = Assertions(browser.driver, verification_errors=[])
browser.driver.get('https://www.amazon.com')


def search_amazon_for(search_string):
    e = browser.driver.find_element_by_locator(locators['main_search_field'])
    e.clear()
    e.send_keys(search_string)
    browser.driver.find_element_by_locator(locators["main_search_button"]).click()
    time.sleep(3)
    try:
        browser.driver.find_element_by_locator(locators["no_results"])
        raise Exception("no results, try another search")
    except NoSuchElementException:
        pass


def refine_search_with(ref, opt):
    refine_by = ref.lower()
    if "price" in refine_by and isinstance(opt, list):
        el = browser.driver.find_element_by_locator(locators['search_price_low'])
        el.clear()
        el.send_keys(price_range[0])
        el = browser.driver.find_element_by_locator(locators['search_price_high'])
        el.clear()
        el.send_keys(price_range[1])
        browser.driver.find_element_by_locator(locators['search_price_go']).click()
    else:
        option = opt.lower()
        ref_dict = get_refine_search_dict()
        if refine_by in ref_dict.keys() and option in ref_dict[refine_by]:
            el = refine_search_dict[refine_by][option]
            if isinstance(el, WebElement):
                WebElement(el).click()
            else:
                browser.driver.find_element_by_locator(el).click()
        else:
            raise Exception('No such option or refine by parameter in the dict')
    time.sleep(3)

if refine_search_dict:
    print("refine search dict is available")


def get_refine_search_dict():
    if not refine_search_dict:
        left_nav_sections = browser.driver.find_elements_by_locator(locators["left_nav_section"])
        refine_search_by_titles = browser.driver.find_elements_by_locator(locators["search_titles"])
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
                        name = WebElement(search_title).find_element_by_locator(
                            locators["following_input_list"]).get_attribute("name")
                        loc = "css=input[type='checkbox'][name='" + name + "']"
                        refine_search_dict[title][option] = CheckBox(browser.driver, loc)
                    elif "customer review" in title:
                        customer_stars = browser.driver.find_elements_by_locator(locators["stars"])
                        for star in customer_stars:
                            option = star.get_attribute("class")
                            num_of_stars = option[option.rfind("-") + 1:]
                            refine_search_dict[title][num_of_stars + " stars & up"] = star
                    else:
                        try:
                            input_list = WebElement(search_title).find_elements_by_locator(
                                locators["following_input_list"])
                            for input_checkbox in input_list:
                                attr = input_checkbox.get_attribute("name")
                                name = WebElement(input_checkbox).find_element_by_locator(
                                    locators["following_input_title"]).text.lower()
                                loc = "css=input[type='checkbox'][name='" + attr + "']"
                                refine_search_dict[title][name] = loc
                        except NoSuchElementException:
                            raise Exception("exception, NOT inputs ")
                        try:
                            i = 1
                            option_list = WebElement(search_title).find_elements_by_locator(
                                locators["following_option_list"])
                            for option in option_list:
                                i += 1
                                name = WebElement(option).find_element_by_locator(locators["option_title"]).text.lower()
                                link = option.get_attribute("href")
                                loc = "css=a[href='" + link[link.find(".com") + 4:] + "']"
                                refine_search_dict[title][name] = loc
                        except NoSuchElementException:
                            raise Exception("exception, NO lists ")
    return refine_search_dict



price_range = [20, 100]
search_string = "ipad air 2 case"
refine_by = "case material"
option = "plastic"
search_amazon_for(search_string)
refine_search_with(refine_by, option)
refine_search_with("price", price_range)

titles, prices, ratings = get_results()
time.sleep(2)
print(len(titles), "\t", titles)
print(len(prices), "\t", prices)
print(len(ratings), "\t", ratings)

assert_that.assert_true(all(i > price_range[0] and i < price_range[1] for i in prices[0:5]))
sort_by("text=Price: Low to High")
time.sleep(2)
titles, prices, ratings = get_results()
print(len(titles), "\t", titles)
print(len(prices), "\t", prices)
print(len(ratings), "\t", ratings)
results_dict = dict(zip(titles, zip(prices, ratings)))
print(results_dict)
#assert_that.assert_true(all(prices[i] <= prices[i+1] for i in range(len(prices)-1)))
sort_by("text=Avg. Customer Review")
time.sleep(20)
titles, prices, ratings = get_results()


print(len(titles), "\t", titles)
print(len(prices), "\t", prices)
print(len(ratings), "\t", ratings)

browser.driver.quit()

