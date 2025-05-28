import turtle

# Setup
screen = turtle.Screen()
robot = turtle.Turtle()
robot.speed(2)
robot.showturtle()
robot.shape("turtle")

robot.pencolor('green')


for i in range(13):
  robot.forward(200)
  robot.left(150)

# Finish
robot.hideturtle()
screen.exitonclick()
