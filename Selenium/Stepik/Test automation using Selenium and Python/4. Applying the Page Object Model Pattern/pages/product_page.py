from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_correct_confirming_message(self):
        confirming_message = self.browser.find_element(*ProductPageLocators.CONFIRMING_MESSAGE).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == confirming_message, "Invalid book name"

    def should_be_correct_basket_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_price, "Invalid book price"

    def confirming_message_should_not_be(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRMING_MESSAGE)

    def confirming_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRMING_MESSAGE)       