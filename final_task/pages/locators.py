from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRMATION_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCTS_CHECKOUT = (By.CSS_SELECTOR, "div.form-group.clearfix > div > div > a")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")