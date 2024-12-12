import turtle
import colorsys

def spiral_star():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(10)
    
    hue = 0
    for i in range(150):
        turtle.color(colorsys.hsv_to_rgb(hue, 1, 1))
        hue += 0.005
        
        for _ in range(5):
            turtle.forward(200 - i)
            turtle.right(144)
        turtle.right(10)
    
    turtle.done()

spiral_star()
