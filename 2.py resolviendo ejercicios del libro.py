#funcion test
import sys 
def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)
#aca termina la funcion TEST
class Punto:
    def __init__(self,absisca,ordenada):
        self.absisca=absisca
        self.ordenada=ordenada
class Rectangle:
    def __init__(self,punto_inicial,ancho,alto):
        self.punto_inicial=punto_inicial
        self.ancho=ancho
        self.alto=alto
    def __mostrar__(self):
        return f"El rectangulo tiene como atributos:\n1-Punto inicial:\n  1.1-Eje de las abscisas: {self.punto_inicial.absisca}\n  1.2-Eje de las ordenadas: {self.punto_inicial.ordenada}\n2-Ancho: {self.ancho}\n3-Alto: {self.alto}"
    def centro(self):
        return f'El centro del rectangle antes mencionado es ({self.punto_inicial.absisca+self.ancho/2} , {self.punto_inicial.ordenada+self.alto/2}) '
    def centro_secundary(self):
        punto=Punto(0,0)
        punto.ordenada=self.punto_inicial.ordenada+self.alto/2
        punto.absisca=self.punto_inicial.absisca+self.ancho/2
        return f"({punto.absisca} , {punto.ordenada})"
    def area(self):
        return self.alto*self.ancho
    def perimetro(self):
        return (2*self.ancho)+(2*self.alto)
    def flip(self):
        a=self.alto
        self.alto=self.ancho
        self.ancho=a
    def contiene(self,punto_arbitrario):
        if self.punto_inicial.absisca<=punto_arbitrario.absisca<self.punto_inicial.absisca+self.ancho and self.punto_inicial.ordenada<=punto_arbitrario.ordenada<self.punto_inicial.ordenada+self.alto:
            return True
        return False
    #def chocan(self,otro_rectangulo):
        
auxiliar_rectangle=Rectangle(Punto(0,0),10,5)
r=Rectangle(Punto(0,0),10,5)
def main():
    print("aca empieza")
    print(auxiliar_rectangle.centro_secundary())
    print("aca termina")
    print(auxiliar_rectangle.__mostrar__())
    print(auxiliar_rectangle.centro())
    print(f"El area es {auxiliar_rectangle.area()}")
    print(f"El perimetro es {auxiliar_rectangle.perimetro()}")
main()
def test_suite():
    test(auxiliar_rectangle.area(),50)
    test(auxiliar_rectangle.perimetro(),30)
    test(auxiliar_rectangle.ancho,10)
    test(auxiliar_rectangle.alto,5)
    auxiliar_rectangle.flip()
    test(auxiliar_rectangle.ancho,5)
    test(auxiliar_rectangle.alto,10)
    test(r.contiene(Punto(3,7)),False)
    test(r.contiene(Punto(3,4.999999)),True)
test_suite()
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        return f"El vehiculo de marca: {self.marca} y modelo: {self.modelo}\nEstado de:\n-Enmarcha:{self.enmarcha}\n-Acelerando:{self.acelera}\n-Frenando:{self.frena}"
class Furgoneta(Vehiculo):
    def cargar(self,carga):
        self.cargado=carga
        if (self.cargado):
            return "La furgoneta esta cargada"
        return "La furgoneta no esta cargada"
class VElectrico:
    def __init__(self,autonomia,cargando):
        self.autonomia=autonomia
        self.cargando=False
    def cargarbateria(self):
        self.cargando=True
class BiciElectrica(Vehiculo,VElectrico):
    pass

class Moto(Vehiculo):
    hacecaballito=False
    #def __init__(self,marca,modelo,frenos)
    def hacercaballo(self):
        self.hacecaballito=True
    def estado(self):
        return f"{Vehiculo.estado(self)}\n-Hace caballo: {self.hacecaballito}"
miMoto=Moto("Halion","La mamalona")
miMoto.arrancar()
miMoto.hacercaballo()
print(miMoto.estado())
miFurgoneta=Furgoneta("Logitech","Ballista")
print(miFurgoneta.cargar(True))
miBici=BiciElectrica("gamemax","HS35")
print(miBici.)
miBici.cargarbateria()
print(miBici.cargarbateria())