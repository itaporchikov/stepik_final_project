from product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.product_name_in_message_should_match_product_added_to_basket()
    page.basket_price_should_be_the_same_as_the_product_price()