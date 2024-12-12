import turtle
import colorsys

def mandala_pattern():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(10)
    turtle.pensize(2)
    
    hue = 0
    for i in range(72):
        turtle.color(colorsys.hsv_to_rgb(hue, 1, 1))
        hue += 0.01
        
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        
        for _ in range(8):
            turtle.forward(200)
            turtle.backward(200)
            turtle.left(45)
        turtle.right(5)
    
    turtle.done()

mandala_pattern()
