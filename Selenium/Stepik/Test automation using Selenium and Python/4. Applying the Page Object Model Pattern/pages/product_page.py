from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        basket.click()

    def compare_product_name(self):
        alert_name = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[0].text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert alert_name == name, "Invalid product name"

    def compare_product_price(self):
        alert_price = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[2].text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert alert_price == price, "Invalid product price"