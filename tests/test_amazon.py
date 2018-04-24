from framework.pages.amazon_main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
from framework.browser import Browser
from framework.assertions import Assertions
from framework.base.FrameTest import FrameTestCase

titles = []
prices = []
price_range = [20, 100]
search_string = "ipad air 2 case"
title1 = "case material"
option1 = "plastic"
title2 = "price"
sort_option1 = "text=Price: Low to High"
sort_option2 = "text=Avg. Customer Review"


class TestAmazon(FrameTestCase):

    def test_search(self):
        page = MainPage(self.driver)
        page.open()
        self.take_numbered_screenshot()
        page.search_amazon_for(search_string)
        self.take_numbered_screenshot()
        page.refine_search_with(title1, option1)
        self.take_numbered_screenshot()
        page.refine_search_with(title2, price_range)
        self.take_numbered_screenshot()
        titles, prices, ratings = page.get_results()
        print(prices[0:5])
        self.assertions.assert_true(all(i > price_range[0] and i < price_range[1] for i in prices[0:5]))
        page.sort_by(sort_option1)
        self.take_numbered_screenshot()
        page.sort_by(sort_option2)
