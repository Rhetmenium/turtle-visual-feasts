import turtle

def snowflake_side(length, levels):
    if levels == 0:
        turtle.forward(length)
        return
    length /= 3.0
    snowflake_side(length, levels - 1)
    turtle.left(60)
    snowflake_side(length, levels - 1)
    turtle.right(120)
    snowflake_side(length, levels - 1)
    turtle.left(60)
    snowflake_side(length, levels - 1)

def fractal_snowflake():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.color("cyan")
    turtle.pensize(2)
    
    for _ in range(3):
        snowflake_side(300, 4)
        turtle.right(120)
    
    turtle.done()

fractal_snowflake()
