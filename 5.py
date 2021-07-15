#first turtle
import  turtle              # Nos permite usar tortugas 
wn  =  turtle . Screen ()
wn.bgcolor("lightblue")
wn.title("Hola este es un repaso rapido")       # Crea un patio de recreo para tortugas 
    # Crea una tortuga, asigna a alex
alex  =  turtle . Turtle ()
alex.speed(100)
alex.pensize(5)

alex.color("black")
alex . forward ( 80)
alex.color("blue")
alex . left ( 90 )              # Dile a Alex que gire 90 grados 
alex . forward ( 80 )           # Completa el segundo lado de un rectángulo
alex . left ( 90 )
alex.color("black")
alex . forward ( 80)
alex.color("blue")
alex . left ( 90 )              # Dile a Alex que gire 90 grados 
alex . forward ( 80 )           # Completa el segundo lado de un rectángulo
alex . left ( 90 )
       
tess  =  turtle . Turtle ()
tess.speed(100)
tess.pensize(5)


tess.forward(80)
tess.left(120)
tess.forward((5**1/2)*40)
tess.left(120)
tess.forward(80)
tess.left(120)


wn . mainloop ()              # Espere a que el usuario cierre la ventana
print("A continuación\nharemos una carta para todos los seres queridos\t que quieras invitar a tu cumpleaños")
a=input("introduce el nombre de tu primer ser querido: ")
b=input("introduce el nombre de tu segundo ser querido: ")
c=input("introduce el nombre de tu tercer ser querido: ")
d=input("introduce el nombre de tu cuarto ser querido: ")
for t in[a,b,c,d]:
    invitational = "Hi "+t+ " please im need you in mi birthday"
    print(invitational)
print("gracias a todos por su atención")