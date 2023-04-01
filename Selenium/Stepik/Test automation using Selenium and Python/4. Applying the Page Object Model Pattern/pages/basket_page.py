from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE, timeout=10), "Basket not empty"
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "Wrong basket section"
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert "Your basket is empty" in text_in_basket