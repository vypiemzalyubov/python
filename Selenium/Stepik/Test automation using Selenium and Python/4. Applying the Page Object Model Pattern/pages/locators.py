from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_LIST = (By.CSS_SELECTOR, '.alertinner strong')   