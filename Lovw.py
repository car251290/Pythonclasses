import turtle

a = turtle.Turtle()
def curvemove():
    for i in range(200):
        a.right(1)
        a.forward(1)
a.color('red','blue')
a.begin_fill()
a.left(140)
a.forward(111.65)
curvemove()
a.left(120)
curvemove()
a.forward(111.65)
a.end_fill()
a.done()


