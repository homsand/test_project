from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest,time

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser,link):
    #link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
 #   page=ProductPage(browser,link)
 #   page.open()
 #   page.add_product_to_basket()
 #   page.should_not_be_success_message()
#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    page=ProductPage(browser,link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_not_be_success_message()

#def test_guest_cant_see_success_message(browser):
#    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    page=ProductPage(browser,link)
#    page.open()
#    page.should_not_be_success_message()
#@pytest.mark.xfail
#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    page=ProductPage(browser,link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_be_success_message_is_disappear()
#def test_guest_should_see_login_link_on_product_page(browser):
#   link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page=ProductPage(browser,link)
#    page.open()
#    page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page(browser):
#    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page=BasePage(browser,link)
#    page.open()
#    page.go_to_login_page()
#    login_page=LoginPage(browser,browser.current_url)
#    login_page.should_be_login_page()

#def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page=BasePage(browser,link)
#    page.open()
#    page.go_to_basket_page()
#    basket_page=BasketPage(browser,browser.current_url)
#    basket_page.should_be_message_basket_is_empty()
#    basket_page.should_not_be_goods_in_basket()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page=LoginPage(browser,link)
        page.open()
        email=str(time.time()) + "@fkmail.org"
        password="wertgkn164"
        page.register_new_user(email,password)
        reg_page=BasePage(browser,browser.current_url)
        reg_page.should_be_authorized_user()
    #def test_register(self,browser):
      #  link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
      #  page=BasePage(browser,link)
      #  page.open()
      #  page.should_be_authorized_user()
    def test_user_cant_see_success_message(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page=ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=ProductPage(browser,link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()
    