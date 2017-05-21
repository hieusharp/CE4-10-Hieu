from turtle import *
speed(-1)
def draw_square():
    for _ in range(4):
        fd(20)
        left(90)
for _ in range(5):
    draw_square()
    penup()
    fd(40)
    pendown()
    
    
