from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_a_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_CHECKOUT), \
            "There are products in a basket"

    def should_be_text_that_a_basket_is_empty(self):
        x = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert x == "Your basket is empty. Continue shopping", f"Wrong text, got '{x}' instead of 'Your basket is empty. Continue shopping'"