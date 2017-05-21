from turtle import *
speed(-1)
def draw_4square(sz):
    for _ in range(4):
        fd(sz)
        lt(90)
    for _ in range(4):
        bk(sz)
        rt(90)
    for _ in range(4):
        fd(sz)
        rt(90)
    for _ in range(4):
        bk(sz)
        lt(90)
x=10
for _ in range(x):
    draw_4square(100)
    lt(360/x)
