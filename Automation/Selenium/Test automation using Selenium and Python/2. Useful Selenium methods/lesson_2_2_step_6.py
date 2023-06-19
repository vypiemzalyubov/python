# Задание на execute_script
# 
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. 
# Вам потребуется написать код, чтобы:
# 
# 1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x.
# 4. Проскроллить страницу вниз.
# 5. Ввести ответ в текстовое поле.
# 6. Выбрать checkbox "I'm the robot".
# 7. Переключить radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("https://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    res_calc = calc(x_element)

    browser.execute_script("window.scrollBy(0, 100);")

    input = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(res_calc)

    button_checkbox = browser.find_element(By.XPATH, "//*[@for='robotCheckbox']").click()
    button_radiobutton = browser.find_element(By.XPATH, "//*[text()='Robots rule']").click()
    
    button_submit = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

finally:
    time.sleep(5)
    browser.quit()