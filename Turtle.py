from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)
def draw_polygon(n):
    for _ in range(n):
        forward(50)
        left(360/n)
    
for n in range(3,8):
    color(colors[n-3])
    draw_polygon(n)
        
penup()
right(90)
forward(100)
left(90)
pendown()

for x in range(len(colors)):
    
    begin_fill()
    color(colors[x])
    draw_polygon(4)
    forward(50)
    end_fill()
