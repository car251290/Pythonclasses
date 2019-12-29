import turtle
import random
a = turtle.Turtle()

for n in range(60):
    a.penup()
    a.goto(random.randint(-400, 400), random.randint(-400, 400))
    a.pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    grey_amount = random.randint( 0,  30) / 100.0
    a.pencolor((red_amount, grey_amount, blue_amount))

    circle_size = random.randint(10, 40)
    a.pensize(random.randint(1, 5))

    for i in range(6):
        a.circle(circle_size)
        a.left(60)
