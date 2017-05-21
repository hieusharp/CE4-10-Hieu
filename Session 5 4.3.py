from turtle import *
speed(-1)
def draw_poly(n,sz):
    for _ in range(n):
        fd(sz)
        left(360/n)
draw_poly(8,50)
