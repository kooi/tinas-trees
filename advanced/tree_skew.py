import turtle

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(0)
tina.setheading(90)
tina.penup()
tina.backward(200)
tina.pendown()
tina.getscreen().colormode(255)
# tina.hideturtle()
tina.getscreen().tracer(0)

def branch(d, a, s, cutoff=5):
    if d > cutoff:
        tina.right(a)
        tina.forward(d)
        branch(s * d, a, s, cutoff=cutoff)
        tina.backward(d)
        tina.left(a)

        tina.left(a)
        tina.forward(d)
        branch(s * d, a, s, cutoff=cutoff)
        tina.backward(d)
        tina.right(a)


def colorbranch(d, a, s, cutoff=5, color=(0,0,0)):
    tina.pencolor(color)
    if d > cutoff:
        tina.right(a)
        tina.forward(d)
        colorbranch(s * d, a, s, cutoff=cutoff, color=color)
        tina.backward(d)
        tina.left(a)

        tina.left(a)
        tina.forward(d)
        colorbranch(s * d, a, s, cutoff=cutoff, color=color)
        tina.backward(d)
        tina.right(a)


def skewcolorbranch(d, a, s, cutoff=5, color=(0,0,0)):
    tina.pencolor(color)
    if d > cutoff:
        tina.right(a*1.5)
        tina.forward(d)
        skewcolorbranch(s * d, a, s, cutoff=cutoff, color=( int(color[0]-d)%255, color[1], color[2]))
        tina.penup()
        tina.backward(d)
        tina.pendown()
        tina.left(a*1.5)

        tina.left(a/1.5)
        tina.forward(d)
        skewcolorbranch(s * d, a, s, cutoff=cutoff, color=( color[0], int(color[1]-d)%255, color[2]))
        tina.penup()
        tina.backward(d)
        tina.pendown()
        tina.right(a/1.5)


tina.penup()
tina.goto(-200,-200)
tina.pendown()

tina.forward(100)
colorbranch(80, 30, .8, cutoff=10, color=(0,196,0))
tina.backward(100)

tina.penup()
tina.goto(200,-200)
tina.pendown()

tina.forward(100)
colorbranch(80, 30, .8, cutoff=10, color=(196,0,0))
tina.backward(100)
    

# tina.forward(100)
# colorbranch(80, 30, .8, cutoff=10)
# tina.backward(100)
# tina.getscreen().update()

# tina.getscreen().exitonclick()
