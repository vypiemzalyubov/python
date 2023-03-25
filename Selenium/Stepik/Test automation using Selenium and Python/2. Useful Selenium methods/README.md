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
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']").click()
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
