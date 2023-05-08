# Задание: использование метода find_elements
# 
# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html). С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта. 
# В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение. 
# Теперь эта задача под силу только роботам.
# 
# Используйте WebDriver, метод find_elements, нужные локатор и его значение. Введите полученный код в качестве ответа к этой задаче.
# 
# В цикле for мы можем последовательно взять каждый элемент из найденного списка текстовых полей и отправить произвольный текст в каждое поле. 
# Если скрипт не успевает заполнить форму, выберите текст покороче.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import string

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.TAG_NAME, "input")
    letters = string.ascii_lowercase
    for element in elements:
        element.send_keys(''.join(random.choice(letters) for _ in range(8)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()