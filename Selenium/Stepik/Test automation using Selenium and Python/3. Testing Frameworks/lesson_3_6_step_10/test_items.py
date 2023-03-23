from selenium.webdriver.common.by import By
import time


def test_basket_button(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    message = browser.find_element(By.XPATH, "//*[contains(@class, 'btn-add-to-basket')]")
    assert message, '"Add to basket" button is missing'