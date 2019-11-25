from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasePageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket=self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket.click()
        BasePage.solve_quiz_and_get_code(self)
        print(self.browser.find_element(*ProductPageLocators.BOOK).text)
        print(self.browser.find_element(*ProductPageLocators.COST).text)
        print(self.browser.find_element(*ProductPageLocators.COMM_BOOK).text)
        print(self.browser.find_element(*ProductPageLocators.COMM_COST).text)
        assert self.browser.find_element(*ProductPageLocators.BOOK).text==self.browser.find_element(*ProductPageLocators.COMM_BOOK).text,"Book correct!"
        assert self.browser.find_element(*ProductPageLocators.COST).text==self.browser.find_element(*ProductPageLocators.COMM_COST).text,"Cost correct!"
              
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
          "Success message is presented, but should not be"

    def should_be_success_message_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
          "Success message is disappear"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
