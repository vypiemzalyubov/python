### Поиск элементов с помощью Selenium
---
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
Пример:  найти кнопку со значением id="submit_button"

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
```
### Отличие find_element и find_elements

Если первый метод не смог найти элемент на странице, то он вызовет ошибку **NoSuchElementException**, которая прервёт выполнение кода. Второй же метод всегда возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и программа перейдет к выполнению следующего шага в коде.
