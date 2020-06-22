import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(2)

# tina onderaan
tina.left(90)
tina.penup()
tina.backward(300)
tina.pendown()
tina.pensize(2)

def tak_links(lengte):
    if lengte > 10:
        tina.left(45)
        tina.forward(lengte)
        tak_links(lengte / 2)
        tak_rechts(lengte / 2)
        tina.backward(lengte)
        tina.right(45)

def tak_rechts(lengte):
    if lengte > 10:
        tina.right(45)
        tina.forward(lengte)
        tak_links(lengte / 2)
        tak_rechts(lengte / 2)
        tina.backward(lengte)
        tina.left(45)

# tak 1
tina.forward(200)

# tak 2
tak_links(150)

# tak 3
tak_rechts(150)

