import  turtle              # Nos permite usar tortugas 
wn  =  turtle . Screen ()
wn.bgcolor("lightblue")       # Crea un patio de recreo para tortugas 
def draw_sequence_squares(alex,sz):
    for t in range(5):
        for j in range (4):
            alex.color("hotpink")
            alex . forward ( sz)
            alex . left ( 90 )
        alex.penup()
        alex.forward(2*sz)
        alex.pendown()
tess=turtle . Turtle () 
tess.speed(15)
tess.pensize(5)
size=50
draw_sequence_squares(tess,size)

wn . mainloop () 