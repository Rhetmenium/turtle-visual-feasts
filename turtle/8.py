import turtle
import math
import colorsys

def butterfly_pattern():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(10)
    
    hue = 0
    for angle in range(360):
        turtle.color(colorsys.hsv_to_rgb(hue, 1, 1))
        hue += 0.005
        
        x = 200 * math.sin(math.radians(angle)) * math.cos(math.radians(angle))
        y = 200 * math.sin(math.radians(angle))
        
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(5)
    
    turtle.done()

butterfly_pattern()
