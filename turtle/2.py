import turtle

def spiral_pattern():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.pensize(2)
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    for i in range(360):
        turtle.color(colors[i % len(colors)])
        turtle.forward(i * 2)
        turtle.left(59)
    
    turtle.done()

spiral_pattern()
