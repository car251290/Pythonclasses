# Pythonclasses
Classes for children to understand Phyton.


Introduction

Turtle graphics is a popular way for introducing programming to kids. Virtual turtles can be programmed to move around the screen. The turtle draws lines as it moves. The "turtle" could look like the turtle animal, an arrow, or be invisibile. The user can write turtle programs that draw beautiful shapes and learn to program at the same time.

The original Turtle software was developed by Wally Feurzig and Seymour Papert in 1966.

This tutorial only explains Python's turtle.py module. It does not explain the Python programming language.



Quickstart

The instructions in your program tell the "turtle" how to move. The turtle draws a line behind it as it moves. This program draws a square. The steps given to the program are:
Move forward 100 steps. (In the beginning, the turtle is facing to the right.)
Turn 90 degrees to the left.
Move forward 100 steps.
Turn 90 degrees to the left.
Move forward 100 steps.
Turn 90 degrees to the left.
Move forward 100 steps. The turtle has ended up where it started.
With these seven steps, the turtle draws a square. The from turtle import * is an instruction needed at the beginning of all of your turtle programs. It imports the turtle module so you can do the turtle instructions.
There are many instructions like left() and forward(). These instructions are called functions. This tutorial explains many of the functions in the turtle module. When you learn more of these functions, you will be able to draw many different shapes and beautiful pictures!
Examples

from turtle import *
for i in range(500): # this "for" loop will repeat these functions 500 times
    forward(i)
    left(91)
    
    
