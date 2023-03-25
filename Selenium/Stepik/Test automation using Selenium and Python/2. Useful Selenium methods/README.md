## Методы Selenium

<details><summary><b>Основные методы</b></summary>

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

---
  
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
