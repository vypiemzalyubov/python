## Selenium

<details><summary><b>Методы Selenium</b></summary>

### Метод get
  
Сообщает браузеру, что нужно открыть сайт по указанной ссылке
```python
driver.get("https://suninjuly.github.io/text_input_task.html")
```  
  
### Метод click

Позволяет найти элемент и нажать на него
```python
button = browser.find_element(By.CSS_SELECTOR, "[value='python']").click()
```  

### Методы find_element и find_elements  
  
Данные методы, в сочетании с классом **By** для выбора атрибутов, могут быть полезны для поиска элементов страницы.

`find_element` - возвращает первый экземпляр из нескольких веб-элементов с определенным атрибутом в DOM. Метод вызывает исключение **NoSuchElementException**, если ни один элемент не соответствует требуемому локатору. 

`find_elements` - возвращает список всех экземпляров веб-элементов, соответствующих определенному атрибуту. Список будет пустым, если в DOM нет нужных элементов.
```python
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//input[name()="password"]')
driver.find_elements(By.XPATH, '//input')  
```  
  
### Метод get_attribute  
  
Позволяет узнать значение атрибута элемента. Значение атрибута представляет собой строку. Если значение атрибута отсутствует, то это равносильно значению атрибута равному "false". Если атрибута нет, то метод вернёт значение None.
```python
people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")  
```  

### Метод execute_script  
  
С помощью метода `execute_script` можно выполнить программу, написанную на языке JavaScript, как часть сценария автотеста в запущенном браузере. Исполняемый JavaScript код нужно заключать в кавычки (двойные или одинарные). Также можно выполнить сразу несколько инструкций, перечислив их через точку с запятой.
```python
# Вызвать alert в браузере  
browser.execute_script("alert('Robots at work');")
  
# Изменить заголовок страницы, затем вызвать alert  
browser.execute_script("document.title='Script executing';alert('Robots at work');")
  
# Проскроллить страницу на 100 пикселей вниз
browser.execute_script("window.scrollBy(0, 100);")
``` 

### Метод select

Класс **Select** предоставляет полезные методы для взаимодействия с раскрывающимися списками, выбора элементов и многого другого. Вначале нужно инициализировать новый объект, передав в него WebElement с тегом **select**. Далее можно найти любой вариант из списка с помощью метода `select_by_value(value)`.

`select_by_visible_text("text")` - ищет элемент по видимому тексту.

`select.select_by_index(index)` - ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. 
```python
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")
```
  
### Метод switch_to_window

Позволяет переключиться на нужное окно. Дескриптор окна передается в качестве аргумента методу `switch_to_window()`.
```python
browser.switch_to.window(window_name)
```  
Чтобы узнать имя новой вкладки, нужно использовать метод `window_handles`, который возвращает массив имён всех вкладок.
```python
new_window = browser.window_handles[1]
```
Также можно запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться.
```python
first_window = browser.window_handles[0]
```  
  
### Настройка ожиданий в Selenium (Selenium Waits)

#### Неявные ожидания (Implicit waits)

Неявное ожидание информирует Selenium WebDriver о необходимости проверять DOM в течение определенного периода времени при попытке найти веб-элемент, который не доступен сразу после загрузки страницы. По умолчанию неявное ожидание равно нулю. Однако, как только мы определяем его, оно устанавливается на время жизни объекта WebDriver.

```python
# На каждый вызов команды find_element WebDriver будет ждать 10 секунд до появления элемента на странице прежде, 
# чем выбросить исключение NoSuchElementException

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.lambdatest.com/")
element = driver.find_element_by_id("testing_form")
```  

#### Явные ожидания (Explicit Waits)
  
Используется, когда мы хотим дождаться выполнения определенного условия, прежде чем продолжить работу. **Explicit Waits** позволяют задать специальное ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью инструментов **WebDriverWait** и **expected_conditions**.  
 
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
# element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
```  

В объекте **WebDriverWait** используется функция **until**, в которую передается правило ожидания, элемент, а также значение, по которому мы будем искать элемент. В модуле **expected_conditions** есть много других правил, которые позволяют реализовать необходимые ожидания, посмотреть их можно [здесь](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions).
  
Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода **until_not**.  
  
```python
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
```    

### Класс Options (Настройка параметров Selenium WebDriver)
  
Класс **Options** в Selenium обычно используется в сочетании с желаемыми возможностями кастомизации Selenium WebDriver. Так можно выполнять различные операции, такие как открытие браузера (Chrome, Firefox, Safari, IE, Edge и т.д.) в режиме увеличения, включение и отключение расширений браузера, отключение режима GPU, отключение всплывающих окон и многое другое.

```python
# Для Chrome

# 1. Импорт опций Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 2. Инициализация опций Chrome
chrome_options = Options()

# 3. Добавление желаемых возможностей
chrome_options.add_argument("--disable-extensions")

# 4.Добавление желаемых возможностей сессии
driver = webdriver.Chrome(chrome_options=chrome_options)  
```  
  
</details>
  
<details><summary><b>Работа с элементами веб-страницы</b></summary>  

### Работа с элементами типа checkbox и radiobutton
  
Checkbox позволяют выбирать/отключать любой из представленных вариантов, а radiobutton позволяют выбрать только один из вариантов.
  
Оба этих элемента создаются при помощи тега **input** со значением атрибута **type** равным **checkbox** или **radio** соответственно.
```html
<input type="checkbox">
<input type="radio">
``` 
Если checkbox или radiobutton выбран, то у элемента появится новый атрибут **checked** без значения.  
```html
<input type="checkbox" checked>
<input type="radio" checked>
```  
Checkboxes могут иметь как одинаковые, так и разные значения атрибута **name**. Radiobuttons объединяются в группу, где все элементы имеют одинаковые значения атрибута **name**, но разные значения атрибута **value**. Поэтому и те, и другие лучше искать с помощью значения **id** или значения атрибута **value**.  
```html
<input type="radio" name="language" value="python" checked>
<input type="radio" name="language" value="selenium">
```   
Тег **label** используется для того, чтобы сделать кликабельным текст, который отображается рядом с checkbox. Элемент **label** связывается с элементом **input** с помощью атрибута **for**, в котором указывается значение атрибута **id** для элемента **input**
```html
<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
```

### Работа со списками
  
Особенности выпадающих списков:
- У каждого элемента списка обычно есть уникальное значение атрибута **value**
- В списках может быть разрешено выбирать как только один, так и несколько вариантов, в зависимости от типа списка
- Визуально списки могут различаться тем, что в одном случае все варианты скрыты в выпадающем меню, а в другом все варианты или их часть видны

```html
<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
 <option selected>--</option>
 <option value="1">Python</option>
 <option value="2">Java</option>
 <option value="3">JavaScript</option>
</select>
```

Варианты ответа задаются тегом **option**, значение **value** может отсутствовать. Можно отмечать варианты с помощью метода `click()`. Для этого сначала нужно применить метод `click()` для элемента с тегом **select**, чтобы список раскрылся, а затем кликнуть на нужный вариант ответа. Но более удобным способом считается использование специального класса **Select** из библиотеки WebDriver.

### Загрузка файлов
  
Для загрузки файлов на веб-странице, можно использовать метод `send_keys`, где в качестве аргумента передается путь к нужному файлу на диске. Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — **os**. Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут **type="file"**. Сначала нужно найти этот элемент с помощью селектора, а затем применить к нему метод `send_keys(file_path)`.
```python
# Если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге 

# импортируем модуль  
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))
# имя файла, который будем загружать на сайт
file_name = "file_example.txt"
# получаем путь к file_example.txt  
file_path = os.path.join(current_dir, file_name)
# отправляем файл  
element.send_keys(file_path)  
```  

### Обработка всплывающих окон и оповещений
  
Существует всего три основных типа всплывающих окон и предупреждений, которые обычно используются в веб-приложениях:
- Simple Alert
- Confirmation Alert
- Prompt Alert

#### driver.switch_to.alert
  
Свойство `switch_to.alert` возвращает открытый в данный момент объект **alert**.  Для этого нужно сначала переключиться на окно с **alert**, а затем принять его с помощью команды `accept()`.
```python
alert = browser.switch_to.alert
alert.accept()  
```
Чтобы получить текст из **alert**, используется свойство `text` объекта **alert**.
```python
alert = browser.switch_to.alert
alert_text = alert.text
```
Для работы с модальным окном **confirm** используются свойства `accept()` и `dismiss()`.
```python
confirm = browser.switch_to.alert
confirm.dismiss()
```  
Модального окно **prompt** имеет дополнительное поле для ввода текста. Чтобы ввести текст, используется метод `send_keys()`.
```python
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
```   
</details>

<details>
<summary><b>Поиск элементов</b></summary>
<br>
<details>
<summary><b>Поиск элементов с помощью Selenium</b></summary>

<br>
  
```python
find_element(By.ID, value)                  #поиск по уникальному атрибуту id элемента

find_element(By.CSS_SELECTOR, value)        #поиск элемента с помощью правил на основе CSS

find_element(By.XPATH, value)               #поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов

find_element(By.NAME, value)                #поиск по атрибуту name элемента

find_element(By.TAG_NAME, value)            #поиск элемента по названию тега элемента

find_element(By.CLASS_NAME, value)          #поиск по значению атрибута class

find_element(By.LINK_TEXT, value)           #поиск ссылки на странице по полному совпадению

find_element(By.PARTIAL_LINK_TEXT, value)   #поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки

find_elements(locator, value)               #поиск нескольких элементов
```
```python
# Пример: найти кнопку со значением id="submit_button"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
```
>**Отличие find_element и find_elements**
>
>Если первый метод не смог найти элемент на странице, то он вызовет ошибку **NoSuchElementException**, которая прервёт выполнение кода. Второй же метод всегда возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и программа перейдет к выполнению следующего шага в коде.
</details>

<details>
<summary><b>Поиск элементов с помощью XPath</b></summary>

<br>
  
**по тегу**
```
//div
```
```
//div//p
```
**по атрибуту**
```
//div[@class='g']
```
```
//*[@id='abc']
```
**по тексту внутри тега**
```
//div[text()='text']
```
```
//div[contains(text(),'text'])
```
```
//span[contains(@class,'LC2Ob'])
```
**по номеру элемента**
```
//ul/li[1]
```
```
//ul/li[last()]
```
```
//ul/li[last()-1]
```  
```
//ol[@class='list news_list']/li[2]//span[@class='news_item-content']
```  
```
//ol[@class='news']/li[position()=1]"))  
```
  
**обращение к соседнему элементу родителя**
```
//span[text()='text']/parent::div/following-sibling::div
```
  
**поиск с использованием AND и OR**
```
//a[@rel='noopener' or @target='_blank']
//a[@rel='noopener' and @target='_blank']
//a[@rel='noopener' and @target='_blank' and contains(@class, 'home-link_black_yes')]
```
  
:bulb: [Xpath cheatsheet](https://devhints.io/xpath)
</details>

<details>
<summary><b>Поиск элементов с помощью CSS селекторов</b></summary>

<br>
  
**универсальный** - применяется ко всем эелементам на странице
```css
*
```
**по тегу**
```css
p
```
**по классу**
```css
.paragraph
```
```css
p.another-class
```
**по id**
```css
#abc
```
```css
h2#www
```
**по атрибуту**
```css
a[href="https://google.com"]
```
**селектор потомков** (контекстный селектор)
```css
.container h3
```
**дочерний селектор** (применяется только к единственному первому ребенку)
```css
.container > p
```
**сестринский селектор** (самый ближайший к элементу)
```css
#heading + span
```
**селектор псевдоклассов**
```css
a:hover
```
**селектор псевдоэлементов**
```css
h1::first-letter
```
</details>

<details>
<summary><b>Поиск элементов в консоли DevTools</b></summary>

<br>
  
**по тегу**
```javascript
$$ ("body")
```
**по id**
```javascript
$$ ("#abc")
```
**по классу**
```javascript
$$ (".appbar")
```
**поиск по трем классам**
```javascript
$$ (".col.rhscol.rhstcs")
```
**найти тег у которого нет указанного класса**
```javascript
$$ ("div:not(.col)")
```
**по атрибуту**
```javascript
$$ ("[role='main']")
```
```javascript
$$ ("div[role]")
```
```javascript
$$ ("div[role*='ai']")
```
```javascript
$$ ("div[role^='ai']")
```
```javascript
$$ ("div[role$='in']")
```
**найти тег вложенный в другой тег**
```javascript
$$ ("div[jscontroller='TxZWcc'] div.liYKde")
```
**найти только ребенка, где тег вложен в другой тег**
```javascript
$$ ("div[jscontroller='TxZWcc'] > div.liYKde")
```
**найти у одного тега другой тег**
```javascript
$$ ("ul li:first-child")
```
```javascript
$$ ("ul li:last-child")
```
```javascript
$$ ("li:nth-child(2)")
```
</details>
</details>

<details><summary><b>Тестовые фреймворки</b></summary>

<br>

<details><summary><b>unittest</b></summary>

<br>

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

<details><summary><b>PyTest</b></summary>

<br>

<details><summary><b>Тестирование с помощью PyTest</b></summary>  

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

<details><summary><b>Использование фикстур в PyTest</b></summary>

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

<details><summary><b>PyTest - маркировка</b></summary>
  
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
  
<details><summary><b>PyTest - параметризация, конфигурирование, плагины</b></summary>
  
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
  
><details><summary<b>testparser</b></summary>
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

Плагин **pytest-rerunfailures** - позволяет перезапускать Flaky-тесты (тесты, которые могут падать из-за трудновоспроизводимых багов).

Установка плагина: `pip install pytest-rerunfailures`
  
Запуск:
```python
pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
  
# --reruns n, где n — это количество перезапусков
# --tb=line - сократить лог с результатми теста   
```  

### Запуск автотестов для разных языков интерфейса
  
Чтобы указать язык браузера с помощью WebDriver, используется класс **Options** и метод **add_experimental_option**.
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)  
``` 
