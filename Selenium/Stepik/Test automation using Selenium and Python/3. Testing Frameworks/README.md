## Тестовые фреймворки

<details><summary><h3>unittest</h3></summary>

Общее правило для всех фреймворков: название тестового метода должно начинаться со слова **"test_"**.  Дальше может идти любой текст, который является уникальным названием для теста:
```python
def test_name_for_your_test():
```
Для unittest существуют собственные дополнительные правила:
- Тесты обязательно должны находиться в специальном тестовом классе.
- Вместо assert должны использоваться специальные assertion методы.
```python
# 1. Импортируем unittest в файл
# 2. Создаем класс, который должен наследоваться от класса TestCase
# 3. Создаем тестовые методы, добавляем ссылку на экземпляр класса self в качестве первого аргумента функции
# 4. Вместо assert используем self.assertEqual()
# 5. Строка запуска программы: unittest.main()
# 6. Запуск: python test_abs_project.py
  
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
```
```python
# Было запущено два теста, один тест выполнился с ошибкой. Место ошибки и пояснение к ней отображаются в логе.

.F

======================================================================

FAIL: test_abs2 (__main__.TestAbs)

----------------------------------------------------------------------

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in test_abs2

    self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

AssertionError: Should be absolute value of a number

----------------------------------------------------------------------

Ran 2 tests in 0.000s

FAILED (failures=1)
```  
</details>
