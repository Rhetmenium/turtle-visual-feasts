import turtle
import colorsys

def nested_circles():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(10)
    hue = 0
    
    for i in range(36):
        turtle.color(colorsys.hsv_to_rgb(hue, 1, 1))
        hue += 0.03
        turtle.penup()
        turtle.goto(0, -i * 10)
        turtle.pendown()
        turtle.circle(10 + i * 10)
    
    turtle.done()

nested_circles()
