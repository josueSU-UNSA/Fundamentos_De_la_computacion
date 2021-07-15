import math
def area_of_circle(radio):
    area = math.pi*radio**2
    print("El resultado es "+str(area))
t =float(input("Introduzca el radio del circulo : "))
area_of_circle(t)
