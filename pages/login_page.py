from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #assert self.browser.current_url, "Login link is not found"
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
      #  assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL),"Login is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS),"Pass is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN),"Btn is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
#        assert True
         assert self.is_element_present(*LoginPageLocators.REG_EMAIL),"Email is not presented"
         assert self.is_element_present(*LoginPageLocators.REG_PASS1),"Pass1 is not presented"
         assert self.is_element_present(*LoginPageLocators.REG_PASS2),"Pass2 is not presented"
         assert self.is_element_present(*LoginPageLocators.REG_BTN),"Btn is not presented"