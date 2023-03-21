# Задание: оформляем тесты в стиле unittest
#  
# Попробуйте оформить тесты из первого модуля в стиле unittest.
# 
# 1. Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# 2. Создайте новый файл
# 3. Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# 4. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# 5. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# 6. Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# 7. Запустите получившиеся тесты из файла 
# 8. Просмотрите отчёт о запуске и найдите последнюю строчку 
# 9. Отправьте эту строчку в качестве ответа на это задание 
# Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. 
# Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

class TestClass(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'first name')]").send_keys("Vypiem")
        input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'last name')]").send_keys("Za Lyubov")
        input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'email')]").send_keys("vypiem@gmail.com")
        input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'phone')]").send_keys("88005353535")
        input5 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'address')]").send_keys("World")
        time.sleep(1)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "WRONG")
        
    def test_reg2(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'first name')]").send_keys("Vypiem")
        input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'last name')]").send_keys("Za Lyubov")
        input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'email')]").send_keys("vypiem@gmail.com")
        input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'phone')]").send_keys("88005353535")
        input5 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'address')]").send_keys("World")
        time.sleep(1)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "WRONG")
        
if __name__ == "__main__":
    unittest.main()