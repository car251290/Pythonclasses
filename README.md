# Pythonclasses
Classes for children to understand Phyton and the basic concept of programming.

(Comming Back with Python Classes and giving soon to new children!)

Pyhton with pychart for children control a drone with Python

<div>
 <img style="width: 15%;height:15%;" src="https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp?fit=800%2C800&ssl=1">
 </div>
 


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
	    

## Python Web and Html 

Python used in the web 
