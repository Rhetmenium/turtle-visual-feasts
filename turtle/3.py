import turtle

def flower_pattern():
    turtle.bgcolor("black")
    turtle.speed(0)
    
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    for i in range(36):
        turtle.color(colors[i % len(colors)])
        for _ in range(2):
            turtle.circle(100, 90)
            turtle.circle(100 // 2, 90)
        turtle.left(10)
    
    turtle.done()

flower_pattern()
