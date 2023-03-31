from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.current_url, "Invalid current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email: str, password: str):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), "Pass field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), "Confirm pass field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Register button not presented"

        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"                