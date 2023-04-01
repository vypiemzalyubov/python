<<<<<<< HEAD
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE, timeout=10), "Basket not empty"
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "Wrong basket section"
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert "Your basket is empty" in text_in_basket
=======
from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE, timeout=1), "Basket not empty"
        assert self.is_element_present(*BasketPageLocators.BASKET_INNER), "Wrong basket section"
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_INNER).text
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert BasketPageLocators.empty_text[language] in text_in_basket, f"{text_in_basket}, {BasketPageLocators.empty_text[language]}"
>>>>>>> c7fe7f9d4ade3789a1dd90c4f119a178dc2286e2
