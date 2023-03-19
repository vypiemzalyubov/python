# Задание: работа с выпадающим списком
# 
# Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.
# 
# Напишите код, который реализует следующий сценарий:
# 
# 1. Открыть страницу https://suninjuly.github.io/selects1.html
# 2. Посчитать сумму заданных чисел
# 3. Выбрать в выпадающем списке значение равное расчитанной сумме
# 4. Нажать кнопку "Submit"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

def calc(num1, num2):
    return str(int(num1) + int(num2))

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    res_calc = calc(num1, num2)
    
    select = Select(browser.find_element(By.XPATH, "//*[@class='custom-select']")).select_by_visible_text(res_calc)

    button_submit = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

finally:
    time.sleep(5)
    browser.quit()