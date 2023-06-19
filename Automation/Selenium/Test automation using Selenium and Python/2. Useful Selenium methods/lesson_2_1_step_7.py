# Задание: поиск сокровища с помощью get_attribute
# 
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. 
# Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
# 
# Ваша программа должна:
# 
# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
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
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    img_element = browser.find_element(By.XPATH, "//*[@id='treasure']")
    valuex_element = img_element.get_attribute("valuex")

    calc_result = calc(valuex_element)
    input = browser.find_element(By.ID, "answer").send_keys(calc_result)

    button_checkbox = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
    button_radiobutton = browser.find_element(By.XPATH, "//*[@id='robotsRule']").click()
    button_submit = browser.find_element(By.XPATH, "//*[text()='Submit']").click()
    
finally:
    time.sleep(10)
    browser.quit()