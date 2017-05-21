##import turtle
##def star(turtle, n, d):
##    for i in range(n):
##        angle = 180.0 - 180.0 / n
##        turtle.forward(d)
##        turtle.right(angle)
##        turtle.forward(d)
##mickey=turtle.Turtle()
##star(mickey,5,100)
##

import turtle

mickey = turtle.Turtle()

mickey.speed(-1)
mickey.hideturtle()

mickey.penup()
mickey.goto(-195,45)
mickey.pendown()

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

def drawTurn(someturtle, degree):
    someturtle.penup()
    someturtle.left(degree)
    someturtle.forward(180)
    someturtle.right(degree)
    someturtle.pendown()
    drawStar(someturtle)
    
for deg in (36, 324, 252, 180, 108):
    drawTurn(mickey, deg)
