## Полезные методы Selenium

<details><summary><b>Основные методы</b></summary>
  
### Метод click

Позволяет найти элемент и нажать на него
```python
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']").click()
```  
  
### Метод get_attribute  
  
Позволяет узнать значение атрибута элемента. Значение атрибута представляет собой строку. Если значение атрибута отсутствует, то это равносильно значению атрибута равному "false".
```python
people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")  
```  
  
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
