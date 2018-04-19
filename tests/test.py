import selenium.webdriver
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
            'main_search_button': 'css=input.nav-input[value="Go"]',
            'left_nav_section': "css=#leftNavContainer>h3",
            'colors': "xpath=following-sibling::ul[2]/li/span/a",
            'stars': "css=ul>div>li>span>a>i[class*='star']",
            'search_titles': "css=#leftNavContainer>h4",
            'following_input_list': "xpath=following-sibling::*[1]/div/li/span/span/div/label/input",
            'following_sibling': "xpath=following-sibling::*[1]",
            'following_input_title': "xpath=following-sibling::*[2]/span",
            'following_option_list': "xpath=following-sibling::*[1]/div/li/span/a",
            'option_title': "xpath=.//span",
            'results_list': "css=li[id^='result_']>div>div:nth-child(3)>div>a",
            'results_title': "xpath=.//div[1]/div[3]/div/a[1]",
            'results_price1': "xpath=.//../../../div[4]/div[1]/a[1]/span[1]",
            'results_price2': "xpath=.//../../../div[5]/div[1]/a[1]/span[1]",
            'sort_by': "css=select[id='sort']",


            }
"""
c=[]
c = Config()
c.prepare()
print(c.__dict__["_data"])
print(os.environ.items())
if "OUTPUT_DIR" in os.environ.keys():
    print("output dir already exists", str(os.environ["OUTPUT_DIR"])[-19:])

if isinstance(c, Config) and hasattr(c, "_data"):
    print("c has data")
    print(len(c.__dict__['_data']))
else:
    print("config not prepared")"""
'''
array_size = 10
number = 10
a = numpy.random.randint(10, size=array_size)
#a=[1,3,6,2,0,4,5,6,1,7]
print(a)
for i in range(array_size-1):
    if a[i]+a[i+1] == number:
        print(a[i], '\t', a[i+1], '\t', "summ equals %s\n" % number)

y = 1
print("y = %s" % y)
def fibR(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibR(n-1)+fibR(n-2)
print("fibo of %s with recursion = " % y, fibR(y))

fibo_array=[]
def fibY(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        yield a
for x in fibY(y):
    fibo_array.append(x)
print("fibo array of %s with generator = " % y, fibo_array)

def fibN(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
print("fibo of %s easy = " % y, fibN(y))

def factorial1(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def factorial2(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print(factorial1(y), factorial2(y), factorial(y))'''

def get_results():
    titles = []
    prices = []
    els = browser.driver.find_elements_by_locator(locators["results_list"])
    for el in els:
        title = el.get_attribute("title")
        try:
            p = WebElement(el).find_element_by_locator(locators['results_price1']).get_attribute("innerHTML")
            if p:
                titles.append(title)
                prices.append(Decimal(p[1:]))
        except NoSuchElementException:
            pass
        print('title %s \t price %s' % (title, p))
    return titles, prices

def sort_by_text(param):
    select_sort_by = Select(browser.driver, (locators["sort_by"]))
    try:
        select_sort_by.__set__(str("text="+param))
    except NoSuchElementException:
        raise ("no such sort option")


def refine_results_by(refine_by, option):
    time.sleep(10)

    print("refine search dict %s" % refine_search_dict)
    print(refine_search_dict[refine_by][option])
    if isinstance(refine_search_dict[refine_by][option], WebElement):
        WebElement(refine_search_dict[refine_by][option]).click()
    else:
        browser.driver.find_element_by_locator(refine_search_dict[refine_by][option]).click()
    time.sleep(10)

price_range = [20, 100]
caps = cap_map['chrome']
br_conf = {"type": "chrome", "profiles": {"darwin": "", "headless": ""}, 'grid filters': {'platform': 'mac', 'version': '23.0.1'}}
conf = {'selenium': {'timeout': 30, 'executor': {'host': '10.0.0.215', 'port': 5555, 'is grid': False}, 'proxy': {'url': '', 'type': ''}}, 'browser': {'type': 'chrome', 'profiles': {'darwin': None, 'profile': None}, 'grid filters': {'platform': 'mac', 'version': '23.0.1'}}, 'sframe': {'base': 'D:\\PROJECTS\\AMAZON', 'default_browser': 'rabbit', 'ci_type': 'jenkins', 'screenshots': {'on_failure': False, 'on_error': True, 'on_finish': False}}}
browser = Browser(br_conf, conf)
assert_that = Assertions(browser.driver, verification_errors=[])
browser.driver.get('https://www.amazon.com')
browser.driver.find_element_by_locator("css=input#twotabsearchtextbox").send_keys("ipad air 2 case")
browser.driver.find_element_by_locator("css=input.nav-input[value='Go']").click()
el = CheckBox(browser.driver, ("css=input[name='s-ref-checkbox-8080061011'][type='checkbox']"))
print(str(el.__get__()))
time.sleep(3)
el = browser.driver.find_element_by_locator("css=#low-price")
el.clear()
el.send_keys(price_range[0])
el = browser.driver.find_element_by_locator("css=#high-price")
el.clear()
el.send_keys(price_range[1])
browser.driver.find_element_by_locator('css=input.a-button-input[type="submit"][value="Go"]').click()
els = browser.driver.find_elements_by_locator('css=li[id^="result"][class*="result"]')
print(len(els))
listofcases = namedtuple('Case', 'name link price rating')
cases = [None]*len(els)
cases[0] = listofcases(name="case1", price=9.99, rating=4.4, link='www.amazon.com')
ratings=[]
hrefs=[]
names=[]
case_materials = []
refine_search_dict = {'delivery day': {'get it today': "css=input[type='checkbox'][name='s-ref-checkbox-8308920011']"}}
left_nav_sections=browser.driver.find_elements_by_locator("css=#leftNavContainer>h3")
refine_search_by_titles=browser.driver.find_elements_by_locator("css=#leftNavContainer>h4")
refine_search_by_options=browser.driver.find_elements_by_locator("css=#leftNavContainer>ul.a-unordered-list")
print(refine_search_by_options)
i=0

'''for ss in refine_search_by_options:
    print(refine_search_by_options[i])
    sss = refine_search_by_options[i].find_element_by_locator("xpath=./following-sibling::*ul/div/li").text
    print(sss)
    i += 1'''
print("max number of lists = ", len(refine_search_by_titles))

if refine_search_dict:
    print ("refine search dict is available")
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
                refine_search_dict[title][option] = CheckBox(browser.driver, loc)
            elif "customer review" in title:
                customer_stars = browser.driver.find_elements_by_locator(locators["stars"])
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
                    raise ("exception, NOT inputs ")
                try:
                    i = 1
                    option_list = WebElement(search_title).find_elements_by_locator(locators["following_option_list"])
                    for option_link in option_list:
                        i += 1
                        name = WebElement(option_link).find_element_by_locator(locators["option_title"]).text.lower()
                        link = option_link.get_attribute("href")
                        loc = "css=a[href='" + link[link.find(".com") + 4:] + "']"
                        refine_search_dict[title][name] = loc
                except NoSuchElementException:
                    raise ("exception, NO lists ")

refine_by = "avg. customer review"
option = "4 stars & up"
b = "4 star"
if refine_by in refine_search_dict.keys() and b in option:
    print("found option %s in list %s" % (b, refine_by))
print("refiny by %s \t the option %s" % (refine_by, option))
if refine_by in refine_search_dict.keys() and option in refine_search_dict[refine_by].keys():
    print("printing element of %s" % refine_search_dict[refine_by][option])

if "soft" in refine_search_dict["case material attributes"]:
    print("case is soft")

if "moko" in refine_search_dict["brand"]:
    print("moko in brand")

if "rubber" in refine_search_dict["case material"]:
    print("rubber in case materials")

print(refine_search_dict.keys())

titles, prices = get_results()
#prices.append(Decimal("12.88"))
assert_that.assert_true(all(a > price_range[0] and a < price_range[1] for a in prices))
sort_by_text("Price: Low to High")
time.sleep(10)
print([i for i in zip(get_results())])
sort_by_text("Avg. Customer Review")
time.sleep(10)
'''
lists = browser.driver.find_elements_by_locator("css=#leftNavContainer>h4")
for list in lists:
    list_title = list.text
    print(list_title)
    if list_title.lower() == "case material":
        print("case material found")
        els2=list.find_elements_by_locator("css=h4+ul>div>li")
        for el in els2:
            print(el.find_elements_by_locator("css=span>span>div>label>span>span").text)
        #els2 = list.find_elements_by_locator("css=h4+ul>div>li>span>span>div>label>span>span")
        #h4 + ul > div > li > span > span > div > label > span > span
        #els2 = list.find_elements_by_locator("xpath=./following-sibling::ul/div/li/span/span/div/label/span/span")
        case_materials = [WebElement(x).get_attribute("innerHTML").lower() for x in els2]

'''
#print(case_materials)
"""
for el in els:
    ele = el.find_element_by_locator("css=a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal")
    name=ele.get_attribute("title")
    href=ele.get_attribute("href")
    print(name, href)
    names.append(name)
    hrefs.append(href)
    try:
        ele = el.find_element_by_locator("css=span.a-offscreen")

 #       ele = el.find_element_by_css_selector("div>div:nth-child(4)>div:nth-child(1)>a>span.a-offscreen")
        price = ele.get_attribute("innerHTML")
    except NoSuchElementException:
        price = "No Amazon price"

    try:
        ele = el.find_element_by_locator("css=span>span>a>i>span")
        rating = ele.get_attribute("innerHTML")
    except NoSuchElementException:
        rating = "No rating yet"
    finally:
        print("rating = ", rating)
        print("price = ", price)
        ratings.append(rating)
        prices.append(price)
"""
print("total num of prices %s" % len(prices))
print(prices)
print(len(ratings))
print(ratings)
print(cases)

browser.driver.quit()
'''

#tc.setup_class()
#tc.setup_method(classmethod)
#print("len is - ", len(os.environ["OUTPUT_DIR"]))
if "OUTPUT_DIR" in os.environ.keys():
    print("length is not null, output dir is created")
    tc.take_numbered_screenshot()
    print(len(os.environ["SCREENSHOTS_DIR"]))
    tc.take_numbered_screenshot()
    print(tc.config)
else:
    raise Exception("configure error") '''

