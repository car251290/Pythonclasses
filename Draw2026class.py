import turtle

# Create the turtle
t = turtle.Turtle()
t.speed(3)

# Draw a square
for i in range(4):
    t.forward(100)
    t.left(90)

# Draw first diagonal
t.left(45)
t.forward(141)

# Go back to center
t.backward(141)
t.right(90)

# Draw second diagonal
t.forward(141)

# Finish
turtle.done()

# second draw 

t = turtle.Turtle()

for i  in range(4):
    t.forward(100)
    t.left(90)

# Finish
turtle.done()