import turtle
import colorsys

def dynamic_flower():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(10)
    
    hue = 0
    for i in range(360):
        turtle.color(colorsys.hsv_to_rgb(hue, 1, 1))
        hue += 0.002  # Renk değişimi
        
        turtle.circle(120)
        turtle.left(59 + i % 5)  # Döngü hareketi
        
    turtle.done()

dynamic_flower()
