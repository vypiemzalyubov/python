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
```
Пример: найти кнопку со значением id="submit_button"

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
```
>**Отличие find_element и find_elements**
>
>Если первый метод не смог найти элемент на странице, то он вызовет ошибку **NoSuchElementException**, которая прервёт выполнение кода. Второй же метод всегда >возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и программа перейдет к выполнению следующего шага в коде.

## Поиск элементов с помощью CSS селекторов

**универсальный** - применяется ко всем эелементам на странице
```
* {
    font-family: Arial, Helvetica, sans-serif;
}
```
**по тегу**
```
p, h1 {
    color: green;
}
```
**по классу**
```
.paragraph {
    color: red;
    font-size: 20px;
}
```
```
p.another-class {
    background-color: aqua;
}
```
**по id**
```
#abc {
    color: lightcoral;
}
```
```
h2#www {
    color: gray;
}
```
**по атрибуту**
```
a[href="https://google.com"] {
    color: blueviolet;
}
```
**селектор потомков** (контекстный селектор)
```
.container h3 {
    background: grey;
}
```
**дочерний селектор** (применяется только к единственному первому ребенку)
```
.container > p {
    text-decoration: line-through;
}
```
**сестринский селектор** (самый ближайший к элементу)
```
#heading + span {
    color: brown;
}
```
**селектор псевдоклассов**
```
a:hover {
    text-decoration: none;
}
```
**селектор псевдоэлементов**
```
h1::first-letter {
    color: burlywood;
}
```

## Поиск в консоли DevTools:

**по тегу**
```
$$ ("body")
```
**по id**
```
$$ ("#abc")
```
**по классу**
```
$$ (".appbar")
```
**поиск по трем классам**
```
$$ (".col.rhscol.rhstcs")
```
**найти тег у которого нет указанного класса**
```
$$ ("div:not(.col)")
```
**по атрибуту**
```
$$ ("[role='main']")
```
```
$$ ("div[role]")
```
```
$$ ("div[role*='ai']")
```
```
$$ ("div[role^='ai']")
```
```
$$ ("div[role$='in']")
```
**найти тег вложенный в другой тег**
```
$$ ("div[jscontroller='TxZWcc'] div.liYKde")
```
**найти только ребенка, где тег вложен в другой тег**
```
$$ ("div[jscontroller='TxZWcc'] > div.liYKde")
```
**найти у одного тега другой тег**
```
$$ ("ul li:first-child")
```
```
$$ ("ul li:last-child")
```
```
$$ ("li:nth-child(2)")
```

## Поиск элементов с помощью XPath

[Xpath cheatsheet](https://devhints.io/xpath)
