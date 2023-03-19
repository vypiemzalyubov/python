# Задание: загрузка файла
# 
# В этом задании в форме регистрации требуется загрузить текстовый файл.
# Напишите скрипт, который будет выполнять следующий сценарий:
# 
# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4. Нажать кнопку "Submit"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.XPATH, "//*[@name='firstname']").send_keys("Vypiem")
    last_name = browser.find_element(By.XPATH, "//*[@name='lastname']").send_keys("Za Lyubov")
    email = browser.find_element(By.XPATH, "//*[@name='email']").send_keys("iloveselenium@gmail.com")

    download_file = browser.find_element(By.XPATH, "//*[@type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "lesson_2_2_step_8.txt"
    file_path = os.path.join(current_dir, file_name)
    download_file.send_keys(file_path)

    button_submit = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

finally:
    time.sleep(5)
    browser.quit()