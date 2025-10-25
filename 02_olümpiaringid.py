import turtle
t = turtle.Turtle()

aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad Aleksei Leonov")
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()

# Kasutades RGB koodi
turtle.colormode(255)
turtle.pencolor(0, 0, 255) #sinine
turtle.pensize(6)
turtle.speed(0)
turtle.circle(50)
turtle.penup()
turtle.goto(-190,0)
turtle.pendown()
turtle.pencolor(0,0,0) # MUST
turtle.circle(50)
turtle.penup()
turtle.goto(-80,0)
turtle.pendown()
turtle.pencolor(255,0,0) #punane
turtle.circle(50)
turtle.penup()
turtle.goto(-250,-50)
turtle.pendown()
turtle.pencolor(255,255,0)#kollane
turtle.circle(50)
turtle.penup()
turtle.goto(-140,-50)
turtle.pendown()
turtle.pencolor(0, 128, 0) #roheline
turtle.circle(50)
turtle.done()



