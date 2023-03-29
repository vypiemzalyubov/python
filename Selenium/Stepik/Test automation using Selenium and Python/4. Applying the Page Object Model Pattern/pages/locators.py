from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//*[@id='login_for']")
    REGISTRATION_FORM = (By.XPATH, "//*[@id='register_for']")