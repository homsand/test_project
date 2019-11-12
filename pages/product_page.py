from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time
class ProductPage(BasePage):
    def add_product_to_basket(self):
      #  self.browser.execute_script("window.scrollBy(0,40);")
        basket=self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket.click()
        BasePage.solve_quiz_and_get_code(self)
        print(self.browser.find_element(*ProductPageLocators.BOOK).text)
        print(self.browser.find_element(*ProductPageLocators.COST).text)
        print(self.browser.find_element(*ProductPageLocators.COMM_BOOK).text)
        print(self.browser.find_element(*ProductPageLocators.COMM_COST).text)
        assert self.browser.find_element(*ProductPageLocators.BOOK).text==self.browser.find_element(*ProductPageLocators.COMM_BOOK).text,"Book correct!"
        assert self.browser.find_element(*ProductPageLocators.COST).text==self.browser.find_element(*ProductPageLocators.COMM_COST).text,"Cost correct!"
        #time.sleep(5)