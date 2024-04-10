from base_page import BasePage
from locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_name_in_message_should_match_product_added_to_basket(self):
        x = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        y = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert x == y, f"Products do not match each other"

    def basket_price_should_be_the_same_as_the_product_price(self):
        x = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        y = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert x == y, f"Basket price and Product price do not match each other"