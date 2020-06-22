import turtle

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(2)

def tak(lengte):
    tina.forward(lengte)
    tina.left(90)
    tak(lengte * 0.9)

tak(100)
