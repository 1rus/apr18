from framework.pages.amazon_main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
from framework.browser import Browser
from framework.assertions import Assertions
from framework.base.FrameTest import FrameTestCase

titles = []
prices = []
price_range = [20, 100]
search_string = "ipad air 2 case"


class TestAmazon(FrameTestCase):

