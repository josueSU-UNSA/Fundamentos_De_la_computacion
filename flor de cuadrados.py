import turtle
def draw_square1 (t,sz):
    for i in ["blue" ]:
        t.color(i)
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz*2)
        t.right(90)
        t.forward(sz*2)
        t.right(90)
        t.forward(sz*2)
        t.right(90)
        t.forward(sz*2)
        t.right(90)
        t.forward(sz*2)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz*2)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(30)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(2)
tess.speed(1)
size = 100
for f in range (1):
    draw_square1 (tess,size)
    


wn.mainloop()
    
 