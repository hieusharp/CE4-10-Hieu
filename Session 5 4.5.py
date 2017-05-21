import turtle
turtle.speed(-1)
turtle.hideturtle()
def draw_spiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(30):
        t.forward(length)
        t.right(angle)
        length = length + 2

mickey=turtle.Turtle()
leo=turtle.Turtle()
leo.pu()
leo.setpos(200,10)
leo.pd()


draw_spiral(mickey, 90)
draw_spiral(leo, 89)
