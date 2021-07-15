#por favor amplie la ventana emergente para que pueda ver las dos imagenes
import turtle
def draw_square1 (t,sz):
    
    t.right(90)
    t.forward(sz)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("yellow","red")
tess.pensize(2)
tess.speed(0)
size = 1
tess.begin_fill()
for f in range (115):
    
    draw_square1 (tess,size)
    size = size+3
tess.end_fill()
tess.right(90)
#parte 2

def draw_squareoblicuo (tortuga,tamaño):
    for i in ["blue" ]:
        tortuga.color(i)
        tortuga.right(89)
        tortuga.forward(tamaño)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
j = turtle.Turtle()
j.pensize(2)
j.speed(50)
t= 1
j.penup()
j.forward(500)
j.pendown()
for f in range (115):
    draw_squareoblicuo (j,t)
    t = t + 3
tess.right(90)
wn.mainloop()