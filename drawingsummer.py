# turtle drawing of sun
import turtle
# basic of turtle graphics
# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

t.color("red")          # turtle color
t.fillcolor("yellow")   # fill shapes
t.pencolor("red")       # outline color
t.speed(3)
# square
t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

# triangle
t.penup()
t.forward(150)
t.pendown()

t.forward(100)
t.left(120)

t.forward(100)
t.left(120)

t.forward(100)
t.left(120)

# circle
t.penup()
t.forward(150)
t.pendown()

t.circle(50)


t.pendown()

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.penup()
t.goto(0, -100)  # center circle
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(100)
t.end_fill()

# --- draw triangles around circle ---
t.penup()
t.goto(0, 0)  # back to center
t.pendown()
t.pencolor("red")
t.fillcolor("yellow")

for i in range(36):  # 36 triangles (every 10 degrees)
    t.penup()
    t.forward(100)   # go to edge of circle
    t.pendown()

    t.begin_fill()
    for _ in range(3):  # draw a triangle
        t.forward(50)
        t.left(120)
    t.end_fill()

    t.penup()
    t.backward(100)  # return to center
    t.left(10)       # rotate for next triangle

screen.mainloop()