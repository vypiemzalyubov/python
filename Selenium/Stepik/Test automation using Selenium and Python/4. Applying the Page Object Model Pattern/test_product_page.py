import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(link, browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_product_name()
    page.compare_product_price()

class TestUserAddToBasketFromProductPage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        email = "test@gmail.com"
        password = "testpassword"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        cart = ProductPage(browser, link)
        cart.open()
        cart.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)       
        page.open()                             
        page.add_to_basket()                    
        page.solve_quiz_and_get_code()
        page.compare_product_name() 
        page.compare_product_price()



def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


