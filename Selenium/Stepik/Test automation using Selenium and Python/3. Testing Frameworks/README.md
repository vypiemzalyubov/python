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

<details><summary><h3>PyTest</h3></summary>

### Установка и запуск
  
Для начала работы с PyTest требуется установить его пакет в виртуальное окружение: `pip install pytest`

Запуск тестов с помощью PyTest: `pytest test_abs_project.py`

### Фиксация пакетов в requirements.txt 

Сохранить все версии пакетов: `pip freeze > requirements.txt`
  
Установить все пакеты из requirements.txt: `pip install -r requirements.txt`
  
### Правила запуска тестов
  
Правила по которым тест-раннер собирает тесты для запуска:

- если мы не передали никакого аргумента в команду, а написали просто `pytest`, тест-раннер начнёт поиск в текущей директории
- как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например: 
```python
# найти все тесты в директории scripts/selenium_scripts
pytest scripts/selenium_scripts

# найти и выполнить все тесты в файле  
pytest test_user_interface.py

# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить  
pytest scripts/drafts.py::test_register_new_user_parametrized
```
- дальше происходит рекурсивный поиск: PyTest обойдет все вложенные директории
- во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  **test_*.py** или ***_test.py** (начинаются на **test_** или заканчиваются **_test** и имеют расширение **.py**)
- внутри всех этих файлов находит тестовые функции по следующему правилу:
  - все тесты, название которых начинается с **test**, которые находятся вне классов
  - все тесты, название которых начинается с **test** внутри классов, имя которых начинается с **Test** (и без метода \_\_init\_\_ внутри класса)  

### PyTest отчёты

В PyTest-отчёте упавший тест выделяется красным шрифтом. Для вывода дополнительной информации со списком тестов и статусом их прохождения используется параметр `-v`

><details><summary><b>Пример отчёта с параметром -v</b></summary>
><img src="https://ucarecdn.com/6a53144b-e083-410f-92ef-404511fc6c07/" style="height: 420px; width:1103px;"/>  
></details>

### PyTest — как пишут тесты
  
PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest. Также, PyTest может запускать тесты, написанные в unittest-стиле.
  
><details><summary><b>Пример простого кода</b></summary>
>
>```python
>def test_abs1():
>    assert abs(-42) == 42, "Should be absolute value of a number"
>
>def test_abs2():
>    assert abs(-42) == -42, "Should be absolute value of a number"  
>```
></details>  
