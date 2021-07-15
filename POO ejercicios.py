class Producto:
    def __init__(self,codigo,nombre,precio):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__precio=precio
    def calculartotal(self,undidades):
        return f"El total seria {self.__precio*undidades}"
    def __str__(self):
        return f"-Nombre del producto:{self.__nombre}\n-Codigo: {self.__codigo}\n-Precio: {self.__precio}"
    def get_Codigo(self):
        return self.__codigo
    def get_Nombre(self):
        return self.__nombre
    def get_Precio(self):
        return self.__precio
    def set_Nombre(self,nombre1):
        self.__nombre=nombre1
def accion(a):
    Pastel=Producto(456560,"Pastel",3.5)
    print(Pastel.get_Codigo())
    print(Pastel.calculartotal(a))
    print(Pastel)
    Pastel.set_Nombre("keke")
    print(Pastel)
c=float(input("Ingrese la cantidad que llevara del producto elegido: "))
accion(c)
'''class Pedido:
    def __init__(self,listadeproductos,listadecantidades):
        self.listadeproductos=listadeproductos
        self.listadecantidades=listadecantidades
    def totalpedido(self,)'''
'''class Time:
    def __init__(self,hora,minuto,segundo):'''
class Vehiculo:
    pass
class Camion(Vehiculo):
    def desplazar(self):
        print("Me desplazo en 6 ruedas")
class Moto(Vehiculo):
    def desplazar(self):
        print("Me desplazo en 2 ruedas")
class Auto(Vehiculo):
    def desplazar(self):
        print("Me despalzo en 4 ruedas")
def polimorphsim(vehiculo):
    vehiculo.desplazar()
hibrido=Camion()
polimorphsim(hibrido)           