import turtle
a = turtle.Turtle()
a.pensize(20)
a.pencolor('red')
a.forward(50)
a.pencolor(0, 1.0, 0)
a.forward(50)
a.pencolor((0, 0.5, 0.5))
a.forward(50)

a.pensize(10)
a.goto(-400, 50)

for red in range(4):
    for grey in range(4):
        for blue in range(4):
            a.pencolor(red / 4.0, grey / 4.0, blue / 4.0)
            a.forward(10)
