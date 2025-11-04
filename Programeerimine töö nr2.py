import turtle

turtle.pensize(3)
turtle.speed(4)

def kujund():
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(170)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

# Kujundi asukohad
positions = [
    (0, 0, 0),        # nkeskel normaalne
    (200, 0, 180),    # tagurpidi
    (100, -100, 90),     # küljepeal vasak
    (100, 100, 270)    # küljepeal parem
]

for x, y, angle in positions:
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()
    kujund()

turtle.hideturtle()
turtle.done()
