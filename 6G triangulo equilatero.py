import turtle

wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Probando funciones")
import turtle
def draw_poly(t,sz,n):
    for f in range (n):
        t.color("hotpink")
        t.forward(sz)
        t.left(360/n)
def draw_equitriangle (l , size,p):
    draw_poly(l,size,p)
tess = turtle.Turtle()
tess.pensize(3)
size = 40
p=3
draw_equitriangle (tess , size,p)
wn.mainloop()
