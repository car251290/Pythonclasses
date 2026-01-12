import math
import turtle

def triangle_equation(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b)- (s-c))
    print("Triangle area:", area)
   
    t = turtle.Turtle()
    t.speed(2)

    t.forward(a * 50)
    t.left(120)

    t.forward(b * 50)
    t.left(120)

    t.forward(c * 50)
    t.left(120)

    turtle.done()
    return area
print(triangle_equation(2,3,4))
    

