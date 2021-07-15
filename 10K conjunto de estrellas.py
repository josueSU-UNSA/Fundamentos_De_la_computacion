import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Probando funciones")
def draw_star (l , size):
    l.right(108)
    for f in range (5):
        l.left(144)
        l.forward(size)
def draw_squence_star (t,sz):
    for l in [ "hotpink"]:
        for i in range (5):
            t.color(l)
            draw_star(t,sz)
            for j in [ "lightgreen"]:
                t.color(j)
                t.forward(200)
                t.right(-36)
tti = turtle.Turtle()
tti.pensize(3)
draw_squence_star(tti ,100)
wn.mainloop()