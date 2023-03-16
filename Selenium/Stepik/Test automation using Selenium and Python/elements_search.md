## Поиск элементов с помощью Selenium

**find_element(By.ID, value)** — поиск по уникальному атрибуту id элемента;

**find_element(By.CSS_SELECTOR, value)** — поиск элемента с помощью правил на основе CSS;

**find_element(By.XPATH, value)** — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;

**find_element(By.NAME, value)** — поиск по атрибуту name элемента;

**find_element(By.TAG_NAME, value)** — поиск элемента по названию тега элемента;

**find_element(By.CLASS_NAME, value)** — поиск по значению атрибута class;

**find_element(By.LINK_TEXT, value)** — поиск ссылки на странице по полному совпадению;

**find_element(By.PARTIAL_LINK_TEXT, value)** — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

**find_elements(locator, value)** - поиск нескольких элементов

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

## Поиск элементов с помощью XPath

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
**обращение к соседнему элементу родителя**
```
//span[text()='text']/parent::div/following-sibling::div
```

:bulb: [Xpath cheatsheet](https://devhints.io/xpath)

## Поиск элементов с помощью CSS селекторов

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

## Поиск элементов в консоли DevTools:

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
