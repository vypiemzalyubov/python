# 203. Напишите программу, которая рисует прямоугольник.
#      Примечание. Программу нужно оформить в виде функции rectangle(width, height), где width, height – ширина и высота прямоугольника.

import turtle

def rectangle(width, height):
  for _ in range(4):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
  
  
rectangle(int(input()), int(input()))

# 204. Напишите программу, которая рисует правильный треугольник.
#      Примечание 1. Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.
#      Примечание 2. Величина каждого угла правильного треугольника равна 60 градусам.

import turtle

def triangle(side):
  for _ in range(3):
    turtle.forward(side)
    turtle.right(240)
  
  
triangle(int(input()))