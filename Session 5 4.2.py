from turtle import *
speed(1)
def draw_square(x):
    for _ in range(4):
        fd(x)
        left(90)
for i in range(5):
    draw_square((i+1)*40)
    pu()
    bk(20)
    rt(90)
    fd(20)
    lt(90)
    pd()
