# На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.
# 
# Ваша программа должна выполнить следующие шаги:
# 
# 1. Открыть страницу https://suninjuly.github.io/math.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x.
# 4. Ввести ответ в текстовое поле.
# 5. Отметить checkbox "I'm the robot".
# 6. Выбрать radiobutton "Robots rule!".
# 7. Нажать на кнопку Submit.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("https://suninjuly.github.io/math.html")
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer").send_keys(y)

    button_checkbox = browser.find_element(By.XPATH, "//*[@for='robotCheckbox']").click()
    button_radiobutton = browser.find_element(By.XPATH, "//*[text()='Robots rule']").click()
    button_submit = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

finally:
    time.sleep(5)
    browser.quit()