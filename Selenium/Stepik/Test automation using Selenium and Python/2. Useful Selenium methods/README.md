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
  
### Метод get_attribute  
  
Позволяет узнать значение атрибута элемента. Значение атрибута представляет собой строку. Если значение атрибута отсутствует, то это равносильно значению атрибута равному "false". Если атрибута нет, то метод вернёт значение None.
```python
people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")  
```  

### Метод select

Класс **Select** предоставляет полезные методы для взаимодействия с раскрывающимися списками, выбора элементов и многого другого. Вначале нужно инициализировать новый объект, передав в него WebElement с тегом **select**. Далее можно найти любой вариант из списка с помощью метода `select_by_value(value)`.
```python
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")
```
  
`select_by_visible_text("text")` ищет элемент по видимому тексту.

`select.select_by_index(index)` ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. 

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

