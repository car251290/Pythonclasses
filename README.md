# Pythonclasses
Classes for children to understand Phyton and the basic concept of programming.

(Comming Back with Python Classes and giving soon to new children!)

# Introduction 

Turtle graphics are a popular way of introducing programming to kids I use this example for the kids to understand the basic concepts of programming virtual turtles can be programmed to move around the screen it is interesting for them because it is like a game because the turtle draws lines as it moves. The "turtle" could look like the turtle animal, an arrow, or be invisible. The kids can write turtle programs that draw beautiful shapes and learn to program at the same time.

The original Turtle software was developed by Wally Feurzig and Seymour Papert in 1966.
This tutorial only explains Python's turtle.py module. It does not explain the Python programming language.

# Quickstart

The instructions in your program tell the "turtle" how to move. The turtle draws a line behind it as it moves. This program draws a square. The steps given to the program are:
Move forward 100 steps. (In the beginning, the turtle is facing to the right.)
Turn 90 degrees to the left.
Move forward 100 steps.
Turn 90 degrees to the left.
Move forward 100 steps.
Turn 90 degrees to the left.
Move forward 100 steps. 
The turtle has ended up where it started.
With these seven steps, 
the turtle draws a square. 

The from turtle import * 
is an instruction needed at the beginning of all of your turtle programs. 
It imports the turtle module so you can do the turtle instructions.
There are many instructions like left() and forward(). 

These instructions are called functions. 
This tutorial explains many of the functions in the turtle module.
When you learn more of these functions, 
you will be able to draw many different shapes and beautiful pictures!

# Examples

from turtle import *
for i in range(500): # this "for" loop will repeat these functions 500 times
    forward(i)
    left(91)
    
   A colorful hexagon spiral program:
    
  from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
    
  # A blue flowers program:
 
from turtle import *
import random

for n in range(60):
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

   red_amount   = random.randint( 0,  30) / 100.0
   blue_amount  = random.randint(50, 100) / 100.0
   green_amount = random.randint( 0,  30) / 100.0
   pencolor((red_amount, green_amount, blue_amount))

   circle_size = random.randint(10, 40)
   pensize(random.randint(1, 5))

   for i in range(6):
       circle(circle_size)
       left(60)
	   
# Moving

By calling these functions, the turtle can be made to move around the screen. Imagine the turtle holding a pen down on the ground and drawing a line as it moves around.

The turtle's position is two numbers: the X coordinate and Y coordinate. The turtle also

# forward(distance)

The forward() function moves the turtle distance number of steps in the current direction. If the pen is down (see pendown() and penup()) a line will be drawn as the turtle moves forward. If distance is a negative number, the turtle will move backwards.

# backward(distance)

The backward() function moves the turtle distance number of steps in opposite direction the current direction. If the pen is down (see pendown() and penup()) a line will be drawn as the turtle moves backward. If distance is a negative number, the turtle will move forward.

# right(angle)

The right() function will change the current direction clockwise by angle degrees. If you imagine being above the turtle looking down, the turtle turning right looks like it is turning clockwise. The turtle will not move; it will only change the direction it is facing.

This example moves the turtle forward, then turns right by 90 degrees, then moves forward again:

This example moves the turtle forward, then turns left by 90 degrees, then moves forward again:

from turtle import *
forward(100)
right(90)
forward(100)

# undo()

The undo() function will undo the turtle's last action. It will be as though the last action was never made. For example, if the last action was a call to the forward(100) function, calling undo will move the turtle backwards 100 steps and erase any line that was drawn. The undo() function can be called many times to erase more and more of the turtle

from turtle import *

for i in range(10):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)

for i in range(30):
    undo()
	
	
 pencolor(), pencolor(color), pencolor((red, green, blue)), pencolor(red, green, blue)

The pencolor() function sets the color of the line that the turtle draws. The pencolor() function can be passed a string of the color, such as 'red' or 'black'. Or, the pencolor() function can be passed an "RGB color tuple" (see the Color section).

from turtle import *

pensize(20)
pencolor('red')
forward(50)
pencolor(0, 1.0, 0)
forward(50)
pencolor((0, 0.5, 0.5))
forward(50)

pensize(10)
goto(-400, 50)

for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red / 4.0, green / 4.0, blue / 4.0)
            forward(10)
