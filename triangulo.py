import turtle

wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Probando funciones")
def draw_triangle (l , size):
    for f in range (3):
        l.forward(size)
        l.left(120)
tti = turtle.Turtle()
draw_triangle (tti,100)
wn.mainloop()