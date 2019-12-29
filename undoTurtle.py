import turtle
a = turtle.Turtle()
for i in range(10):
    a.forward(100)
    a.left(90)
    a.forward(10)
    a.left(90)
    a.forward(100)
    a.right(90)
    a.forward(10)
    a.right(90)

for i in range(40):
    a.undo()
