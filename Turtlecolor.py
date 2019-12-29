import turtle
a = turtle.Turtle()

from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    a.pencolor(colors[x % 6])
    a.width(x / 100 + 1)
    a.forward(x)
    a.left(59)
