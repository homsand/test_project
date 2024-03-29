from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_INVALID=(By.CSS_SELECTOR,"#login_link_inc")
    BASKET_BTN=(By.CSS_SELECTOR,".btn-group a")
    BASKET_MESSAGE=(By.CSS_SELECTOR,"#content_inner p")
    BASKET_GOODS=(By.CSS_SELECTOR,".col-sm-6")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
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
class ProductPageLocators():
    BASKET_BTN=(By.CSS_SELECTOR,".btn-add-to-basket")
    BOOK=(By.CSS_SELECTOR,".product_main h1")
    COST=(By.CSS_SELECTOR,'.product_main p[class="price_color"]')
    COMM_BOOK=(By.CSS_SELECTOR, ".alertinner :nth-child(1)")
    COMM_COST=(By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, ".alertinner :nth-child(1)")