import turtle

# Create turtle variable
robot = turtle.Turtle()
screen = turtle.Screen()

# Draw Square
robot.color("blue")
for i in range(4):
    robot.forward(100)
    robot.left(90)

# Move to draw Triangle
robot.penup()
robot.goto(-150, 0)
robot.pendown()

robot.color("red")
for i in range(3):
    robot.forward(100)
    robot.left(120)

# Move to draw Circle
robot.penup()
robot.goto(150, 0)
robot.pendown()

robot.color("green")
robot.circle(50)

# Finish
screen.exitonclick()