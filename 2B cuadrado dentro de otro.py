import turtle
def draw_square (t,sz):
    for j in range (4):
        t.color("hotpink")
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(3)
tess.speed(0)
size = 20
for f in range (10):
    draw_square (tess,size)
    size = size + 20
    tess.right(135)
    for t in ["lightgreen" ]:
        tess.color(t)
        tess.forward(10*2**(1/2))
    tess.left(135)
 

        
    
    
    
wn.mainloop()