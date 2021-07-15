import turtle

wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Probnado funciones")
def draw_rectangle (p, a,h):
    for n in range(2):
        p.forward(a)
        p.left(90)
        p.forward(h)
        p.left(90)
def draw_square(n,l):
    for f in range(2):
        draw_rectangle (n,l,l)
nn = turtle.Turtle()
draw_square (nn,50)


wn.mainloop()