# Задание: поиск элемента по XPath
# 
# На этот раз воспользуемся возможностью искать элементы по XPath. 
# 
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки. 
# Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё. 
# 
# Ваши шаги: 
# 
# 1. В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# 2. Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# 3. Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# 4. Запустите ваш код.
# 
# Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве ответа на это задание.

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Vypiem")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Za Lyubov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//*[text()='Submit']")
    button.click()

finally:
    time.sleep(20)
    browser.quit()