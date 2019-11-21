from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasePageLocators
import time
class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_GOODS), \
            "Goods are in basket but should not be"
    def should_be_message_basket_is_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*BasePageLocators.BASKET_MESSAGE).text, "Корзина пуста"