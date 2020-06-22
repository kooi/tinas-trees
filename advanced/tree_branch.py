import turtle

tina = turtle.Turtle()
tina.speed(1)
cutoff = 50

def branch(d):
    tina.right(45)
    tina.forward(d)
    branch(d*.5)
    tina.backward(d)
    tina.left(45)
    tina.left(45)
    tina.forward(d)
    branch(d*.5)
    tina.backward(d)
    tina.right(45)

tina.setheading(90)
tina.forward(100)
branch(50)
tina.backward(100)


tina.getscreen().exitonclick()

