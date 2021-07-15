import turtle
def draw_poly(t,sz,n):
    for f in range (n):
        t.color("hotpink")
        t.forward(sz)
        t.left(360/n)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(3)
size = 40
p=8
draw_poly (tess , size,p)
wn.mainloop()
    

