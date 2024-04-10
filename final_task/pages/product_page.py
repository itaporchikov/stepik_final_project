from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def product_name_in_message_should_match_product_added_to_basket(self):
        x = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        y = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert x == y, f"Products do not match each other"

    def basket_price_should_be_the_same_as_the_product_price(self):
        x = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        y = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert x == y, f"Basket price and Product price do not match each other"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Success message is success_message_disappeared, but should not be"