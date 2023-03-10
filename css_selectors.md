### CSS селекторы:

**Универсальный** - применяется ко всем эелементам на странице
```
* {
    font-family: Arial, Helvetica, sans-serif;
}
```
**По тегу**
```
p, h1 {
    color: green;
}
```
**По классу**
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
**По id**
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
**По атрибуту**
```
a[href="https://google.com"] {
    color: blueviolet;
}
```
**Селектор потомков (контекстный селектор)**
```
.container h3 {
    background: grey;
}
```
**Дочерний селектор (применяется только к единственному первому ребенку)**
```
.container > p {
    text-decoration: line-through;
}
```
**Сестринский селектор (самый ближайший к элементу)**
```
#heading + span {
    color: brown;
}
```
**Селектор псевдоклассов**
```
a:hover {
    text-decoration: none;
}
```
**Селектор псевдоэлементов**
```
h1::first-letter {
    color: burlywood;
}
```
