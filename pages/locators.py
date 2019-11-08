from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")
class LoginPageLocators():
    LOGIN_EMAIL=(By.CSS_SELECTOR,'input[name="login-username"]')
    LOGIN_PASS=(By.CSS_SELECTOR,'input[name="login-password"]')
    LOGIN_BTN=(By.CSS_SELECTOR,'button[name="login_submit"]')
    REG_EMAIL=(By.CSS_SELECTOR,'input[name="registration-email"]')
    REG_PASS1=(By.CSS_SELECTOR,'input[name="registration-password1"]')
    REG_PASS2=(By.CSS_SELECTOR,'input[name="registration-password2"]')
    REG_BTN=(By.CSS_SELECTOR,'button[name="registration_submit"]')