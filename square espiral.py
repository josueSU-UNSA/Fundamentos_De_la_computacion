#codigo de espiral de cuadrados
import turtle

wn=turtle.Screen()
wn.bgcolor("yellow")
wn.title("hello im a josue")
def draw_square (t,sz):
    for i in ["red","purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(0)
tess.pensize(2)
size =20
for f in range (15):
    draw_square (tess , size)
    size = size + 10
    tess.forward(10)
    tess.right(18)
#este es otro codigo el mismo pero del profesor
def draw_square (t,sz):
    for i in ["red","purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(2)
tess.speed(0)

for f in range (10,160,10):
    draw_square (tess , f)
    tess.forward(10)
    tess.right(18)
#este codigo es otra cosa
def dibuja_un_rectangulo(tortuga,largo, alto):
    for t in range (2):
        tortuga.stamp()#se estampea donde acaba el primer ciclo en este caso en la tercera esquina 
        tortuga.forward(largo)
        tortuga.left(90)
        tortuga.forward(alto)
        tortuga.left(90)
def dibuja_un_cuadrado(x,size):
    dibuja_un_rectangulo(x,size, size)
alex=turtle.Turtle()
alex.speed(0)
alex.shape("circle")
p=100
dibuja_un_cuadrado(alex,p)
wn.mainloop()



    