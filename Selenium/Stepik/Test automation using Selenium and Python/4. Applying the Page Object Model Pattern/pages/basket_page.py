from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def cart_page(self):
        self.should_be_cart_page()
        self.cart_is_empty()
        self.should_not_be_items_in_cart()

    def cart_is_empty(self):
        cart = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert "Your basket is empty" in cart.text

    def should_be_cart_page(self):
        assert "/en-gb/basket/" in self.browser.current_url, "May be not 'card/basket' page"

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Item(s) in cart but shouldn't be"