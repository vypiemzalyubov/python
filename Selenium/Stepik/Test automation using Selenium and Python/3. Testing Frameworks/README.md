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

<details><summary><h4>Тестирование с помощью PyTest</h4></summary>  

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

### PyTest - отчёты

В PyTest-отчёте упавший тест выделяется красным шрифтом. Для вывода дополнительной информации со списком тестов и статусом их прохождения используется параметр `-v`, для того, чтобы увидеть текст, который выводится командой print() `-s`.

><details><summary><b>Пример отчёта с параметром -v</b></summary>
><img src="https://ucarecdn.com/6a53144b-e083-410f-92ef-404511fc6c07/" style="height: 420px; width:1103px;"/>  
></details>

### PyTest - как пишут тесты
  
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

### PyTest - проверка ожидаемого результата (assert)

В PyTest используется стандартный **assert** метод из языка Python для проверки ожидаемого результата.

```python
assert a == b, "Значения разные"
  
assert user_is_authorised(), "User is guest"  
```  
С помощью **assert** можно проверять любую конструкцию, которая возвращает **True/False**. Это может быть проверка равенства, неравенства, содержания подстроки в строке или любая другая вспомогательная функция, которую можно описать самостоятельно. 

Если нужно проверить, что тест вызывает ожидаемое исключение, можно использовать конструкцию **with pytest.raises()**.

><details><summary><b>Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент</b></summary>
>
>```python
>import pytest
>
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>from selenium.common.exceptions import NoSuchElementException
>
>
>def test_exception1():
>    try:
>        browser = webdriver.Chrome()
>        browser.get("http://selenium1py.pythonanywhere.com/")
>        with pytest.raises(NoSuchElementException):
>            browser.find_element(By.CSS_SELECTOR, "button.btn")
>            pytest.fail("Не должно быть кнопки Отправить")
>    finally: 
>        browser.quit()
>
>def test_exception2():
>    try:
>        browser = webdriver.Chrome()
>        browser.get("http://selenium1py.pythonanywhere.com/")
>        with pytest.raises(NoSuchElementException):
>            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
>            pytest.fail("Не должно быть кнопки Отправить")
>    finally: 
>        browser.quit()
>```  
>В первом тесте элемент будет найден, поэтому ошибка **NoSuchElementException**, которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.
>```python
>test_3_3_9_pytest_raises.py:8 (test_exception1)
>E   Failed: Не должно быть кнопки Отправить
>```  
>Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет.
></details>  
</details>

<details><summary><h4>Использование фикстур в PyTest</h4></summary>

### Классические фикстуры (fixtures)
  
Фикстуры в контексте PyTest - это вспомогательные функции для тестов, которые не являются частью тестового сценария.

Фикстуры можно использовать для разных целей: для подключения к базе данных, с которой работают тесты, создания тестовых файлов или подготовки данных в текущем окружении с помощью API-методов. Одно из распространенных применений фикстур - это подготовка тестового окружения и очистка тестового окружения и данных после завершения теста. 

Классический способ работы с фикстурами - создание **setup** и **teardown** методов в файле с тестами.

Фикстуры можно создавать для модулей, классов и отдельных функций. 
  
><details><summary><b>Фикстура для инициализации браузера</b></summary>
>  
>```python
># Вынесем инициализацию и закрытие браузера в фикстуры, чтобы не писать этот код для каждого теста.
># Реализуем автоматическое закрытие браузера по окончанию тестов.
># Будем сразу объединять наши тесты в тест-сьюты, роль тест-сьюта будут играть классы, в которых мы будем хранить наши тесты.
># Рассмотрим два примера: создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта и создание браузера для каждого теста во втором тест-сьюте.
>
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>link = "http://selenium1py.pythonanywhere.com/"
>
>
>class TestMainPage1():
>
>    @classmethod
>    def setup_class(self):
>        print("\nstart browser for test suite..")
>        self.browser = webdriver.Chrome()
>
>    @classmethod
>    def teardown_class(self):
>        print("quit browser for test suite..")
>        self.browser.quit()
>
>    def test_guest_should_see_login_link(self):
>        self.browser.get(link)
>        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
>
>    def test_guest_should_see_basket_link_on_the_main_page(self):
>        self.browser.get(link)
>        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
>
>
>class TestMainPage2():
>
>    def setup_method(self):
>        print("start browser for test..")
>        self.browser = webdriver.Chrome()
>
>    def teardown_method(self):
>        print("quit browser for test..")
>        self.browser.quit()
>
>    def test_guest_should_see_login_link(self):
>        self.browser.get(link)
>        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
>
>    def test_guest_should_see_basket_link_on_the_main_page(self):
>        self.browser.get(link)
>        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
>```
>
>Вывод в консоли:
><img src="https://ucarecdn.com/e4d862f8-8d75-4a59-9387-f967790f8d09/" style="height: 474px; width:984px;"/> 
>В первом тест-сьюте браузер запустился один раз, а во втором - два раза.
>
>Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста, поэтому лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее. К тому же если вдруг браузер зависнет в одном тесте, то другие тесты не пострадают, если они запускаются каждый в собственном браузере.  

### Фикстуры, возвращающие значение
  
Фикстуры могут возвращать значение, которое затем можно использовать в тестах. Можно создадать фикстуру **browser**, которая будет создавать объект WebDriver. Этот объект будет использоваться в тестах для взаимодействия с браузером. Для этого нужно написать метод **browser** и указать, что он является фикстурой с помощью декоратора **@pytest.fixture**. После этого можно вызывать фикстуру в тестах, передав ее как параметр. По умолчанию фикстура будет создаваться для каждого тестового метода, то есть для каждого теста запустится свой экземпляр браузера.  
  
><details><summary><b>Пример кода</b></summary>
>  
>```python
>import pytest
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>
>link = "http://selenium1py.pythonanywhere.com/"
>
>
>@pytest.fixture
>def browser():
>    print("\nstart browser for test..")
>    browser = webdriver.Chrome()
>    return browser
>
>
>class TestMainPage1():
>    # вызываем фикстуру в тесте, передав ее как параметр
>    def test_guest_should_see_login_link(self, browser):
>        browser.get(link)
>        browser.find_element(By.CSS_SELECTOR, "#login_link")
>
>    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
>        browser.get(link)
>        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
>```
  
### Финализаторы — закрытие браузера
  
Финализаторы позволяют явно закрывать браузеры, после каждого теста. Один из вариантов финализатора — использование ключевого слова **yield**. После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом **yield**.
    
```python
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
```  
 
### Область видимости scope
  
Для фикстур можно задавать область покрытия фикстур. Допустимые значения: **"function"**, **"class"**, **"module"**, **"session"**. Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии. 
  
```python
@pytest.fixture(scope="class")  
```  
  
### Автоиспользование фикстур
  
При описании фикстуры можно указать дополнительный параметр **autouse=True**, который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова.  
  
><details><summary><b>Пример кода</b></summary>
>  
>```python
>import pytest
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>
>link = "http://selenium1py.pythonanywhere.com/"
>
>
>@pytest.fixture
>def browser():
>    print("\nstart browser for test..")
>    browser = webdriver.Chrome()
>    yield browser
>    print("\nquit browser..")
>    browser.quit()
>
>@pytest.fixture(autouse=True)
>def prepare_data():
>    print()
>    print("preparing some critical data for every test")
>
>
>class TestMainPage1():
>    def test_guest_should_see_login_link(self, browser):
>        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
>        browser.get(link)
>        browser.find_element(By.CSS_SELECTOR, "#login_link")
>
>    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
>        browser.get(link)
>        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
>```  
  
</details>  

<details><summary><h4>PyTest - маркировка</h4></summary>
  
Для выборочного запуска тестов в PyTest используется маркировка тестов или **метки (marks)**. Для маркировки теста нужно написать декоратор вида **@pytest.mark.mark_name**, где **mark_name** — произвольная строка.
  
><details><summary><b>Разделить тесты на smoke и regression</b></summary>
>  
>```python
>import pytest
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>
>link = "http://selenium1py.pythonanywhere.com/"
>
>
>@pytest.fixture(scope="function")
>def browser():
>    print("\nstart browser for test..")
>    browser = webdriver.Chrome()
>    yield browser
>    print("\nquit browser..")
>    browser.quit()
>
>
>class TestMainPage1():
>
>    @pytest.mark.smoke
>    def test_guest_should_see_login_link(self, browser):
>        browser.get(link)
>        browser.find_element(By.CSS_SELECTOR, "#login_link")
>
>    @pytest.mark.regression
>    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
>        browser.get(link)
>        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
>```
  
Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр **-m** и нужную метку: `pytest -s -v -m smoke test_fixture.py`
  
Для регистрации меток нужно создать файл **pytest.ini** в корневой директории проекта и добавьте в файл следующие строки:
```python
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
```  
Текст после знака ":" является поясняющим - его можно не писать.  
  
Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать **инверсию**. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
```python
pytest -s -v -m "not smoke" test_fixture.py
```  

Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустить smoke и regression-тесты:
```python
pytest -s -v -m "smoke or regression" test_fixture.py  
```  
  
### Пропуск тестов
  
В PyTest есть стандартные метки, которые позволяют пропустить тест при сборе тестов для запуска (то есть не запускать тест) или запустить, но отметить особенным статусом тот тест, который ожидаемо упадёт из-за наличия бага, чтобы он не влиял на результаты прогона всех тестов. Эти метки не требуют дополнительного объявления в pytest.ini. Чтобы пропустить тест, его отмечают в коде как **@pytest.mark.skip**.

### XFail: помечать тест как ожидаемо падающий

При добавлении маркировки **@pytest.mark.xfail** для падающего теста, результат прогона будет показан как успешный, а отмеченный тест будет помечен как **xfail**.  Когда тест будет проходить, он будет отмечен как **XPASS** ("unexpectedly passing" — неожиданно проходит). После этого маркировку **xfail** для теста можно удалить. К маркировке **xfail** можно добавлять параметр **reason**. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest **-rx**: `pytest -rx -v test_fixture.py`. Чтобы получить подробную информацию по XPASS-тестам можно добавить параметр X: `pytest -rX -v test_fixture.py`
</details>
  
<details><summary><h4>PyTest - параметризация, конфигурирование, плагины</h4></summary>
  
### Conftest.py - конфигурация тестов 
  
Для хранения часто употребимых фикстур и хранения глобальных настроек используется файл **conftest.py**, который должен лежать в директории верхнего уровня в проекте с тестами. Можно создавать дополнительные файлы **conftest.py** в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях. PyTest автоматически находит и подгружает файлы **conftest.py**, которые находятся в директории с тестами. 
  
><details><summary><b>conftest.py с фикстурой browser</b></summary>
>  
>```python
>import pytest
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>
>@pytest.fixture(scope="function")
>def browser():
>    print("\nstart browser for test..")
>    browser = webdriver.Chrome()
>    yield browser
>    print("\nquit browser..")
>    browser.quit()
>```
></details>
  
Фикстура передается в тестовый метод в качестве аргумента. Таким образом можно переиспользовать одни и те же вспомогательные функции в разных частях проекта.
  
### Параметризация тестов
  
PyTest позволяет запустить один и тот же тест с разными входными параметрами. Для этого используется декоратор **@pytest.mark.parametrize()**.
  
В **@pytest.mark.parametrize()** нужно передать параметр, который должен изменяться, и список значений параметра. В самом тесте параметр тоже нужно передавать в качестве аргумента. Внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов теста кавычки не нужны.  

><details><summary><b>Передать в параметрах русский и английский язык</b></summary>
>
>```python  
>import pytest
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>
>@pytest.fixture(scope="function")
>def browser():
>    print("\nstart browser for test..")
>    browser = webdriver.Chrome()
>    yield browser
>    print("\nquit browser..")
>    browser.quit()
>
>@pytest.mark.parametrize('language', ["ru", "en-gb"])
>def test_guest_should_see_login_link(browser, language):
>    link = f"http://selenium1py.pythonanywhere.com/{language}/"
>    browser.get(link)
>    browser.find_element(By.CSS_SELECTOR, "#login_link")
>```
></details>  
   
Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились с заданными параметрами. В таком случае отметка о параметризации должна быть перед объявлением класса.
  
### Использование других браузеров
  
Параметр `browser_name` позволяет передавать название браузера, который нужно запустить:
```python
pytest -s -v --browser_name=firefox test_cmd.py  
```  
  
### Conftest.py и передача параметров в командной строке
  
Передача параметров через командную строку делается с помощью встроенной функции **pytest_addoption** и фикстуры **request**, которая может получать данные о текущем запущенном тесте.
  
Сначала добавляем в файле **conftest** обработчик опции в функции **pytest_addoption**, затем напишем фикстуру, которая будет обрабатывать переданные в опции данные. Добавим логику обработки командной строки в **conftest.py**. Для запроса значения параметра можно вызвать команду:

```python
browser_name = request.config.getoption("browser_name")
```  
  
><details><summary><b>conftest.py</b></summary>
>
>```python  
>import pytest
>from selenium import webdriver
>
>def pytest_addoption(parser):
>    parser.addoption('--browser_name', action='store', default=None,
>                     help="Choose browser: chrome or firefox")
>
>
>@pytest.fixture(scope="function")
>def browser(request):
>    browser_name = request.config.getoption("browser_name")
>    browser = None
>    if browser_name == "chrome":
>        print("\nstart chrome browser for test..")
>        browser = webdriver.Chrome()
>    elif browser_name == "firefox":
>        print("\nstart firefox browser for test..")
>        browser = webdriver.Firefox()
>    else:
>        raise pytest.UsageError("--browser_name should be chrome or firefox")
>    yield browser
>    print("\nquit browser..")
>    browser.quit()
>```
></details>  
  
><details><summary<b>>test_parser.py</b></summary>
>
>```python
>link = "http://selenium1py.pythonanywhere.com/"
>
>
>def test_guest_should_see_login_link(browser):
>    browser.get(link)
>    browser.find_element(By.CSS_SELECTOR, "#login_link")
>```
></details>  

Если запустит тесты без параметра - `pytest -s -v test_parser.py`, то произойдет ошибка. 
  
Также, можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было указывать параметр `--browser_name`:
```python
parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")  
```  
  
### Плагины и перезапуск тестов  
