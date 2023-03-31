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