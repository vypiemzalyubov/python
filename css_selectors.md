### CSS селекторы:

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
### Поиск в консоли DevTools:

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
$$ ("#abc")
```
