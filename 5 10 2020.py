
def distance_of_2points(x1,y1,x2,y2):
    a = abs(x2-x1)
    b = abs(y2-y1)
    c= (a**2 + b**2)**(1/2)
    return c
a=int(input("introduce el valor de la abscisa de tu primera coordenada"))
b=int(input("introduce el valor de la ordenada de tu primera coordenada"))
c=int(input("introduce el valor de la abscisa de tu segunda coordenada"))
d=int(input("introduce el valor de la ordenada de tu primera coordenada"))
ex = distance_of_2points(a, b, c, d)
print(ex)
def buscar_una_distancia_entre_dos_puntos (x,y,x1,y1):
    z= (((x-x1)**2)+((y-y1)**2))**0.5
    print(z)

a=int(input("introduce el valor de la abscisa de tu primera coordenada"))
b=int(input("introduce el valor de la ordenada de tu primera coordenada"))
c=int(input("introduce el valor de la abscisa de tu segunda coordenada"))
d=int(input("introduce el valor de la ordenada de tu primera coordenada"))
buscar_una_distancia_entre_dos_puntos(a,b,c,d)

