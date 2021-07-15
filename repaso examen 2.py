import turtle
def draw_bar (t,altura): 
    "" "Haz que la tortuga t dibuje una barra, de altura." "" 
    t . begin_fill ()            # Agregó esta línea 
    
    t . lt( 90 ) 
    t . fd( altura ) 
    t . write( "" +  str ( altura )) 
    t . rt( 90 ) 
    t . fd ( 40 ) 
    t . right (90 ) 
    t . fd( altura ) 
    t . left ( 90 ) 
    t . end_fill ()              # Agregó esta línea 
    t.penup()
    t . fd( 10 ) 
    t.pendown()
wn  =  turtle.Screen ()          # Configure la ventana y sus atributos 
wn . bgcolor ( "lightgreen" ) 
tess  =  turtle.Turtle ()        # Crea tess y establece algunos atributos 
tess.color("blue","red") 
tess.shape("turtle")
tess.pensize (3) 
xs  =  [ 48 , 117 , 200 , 240 , 160 , 260 , 220 ] 
for a in xs : 
    draw_bar (tess,a) 

wn . mainloop ()