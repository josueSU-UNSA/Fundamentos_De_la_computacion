#Objeto: Es todo aquello que nos rodea abstrayendolo en la programacion como objeto.
#Clase:Ejm un patrullero y un taxi son carros pero tienen diferentes caracteristicas al sacar las caracteristicas externas de ambos entonces tenemos un molde O TAMBIEN PUEDE SER UN CONTENEDOR DE ESTOS OBJETOS
class Perro:
    pelaje=""
    edad=4
    onomatopeya= "ladrar"
    numero_de_patas=4
boby = Perro()
print(boby.numero_de_patas)
print(Perro.onomatopeya)
#clases y objetos II
class nombre:
    pass#saltea esta parte 
josue=nombre()
robert=nombre()
#objeto.atributo=valor
josue.edad=17
josue.altura=1.75
robert.edad=18
robert.altura=1.70
print(josue.edad)
#Las funciones dentro de la clase es un metodo
class Operaciones_matematicas:
    def suma(self):
        self.n1=5
        self.n2=10
operation_1=Operaciones_matematicas()
operation_1.suma()
print(operation_1.n1+operation_1.n2)
#constructor metodo
class Calculadora:
    def __init__(self,n1,n2):
        self.suma=n1+n2
        self.resta=n1-n2
        self.multiplicacion=n1*n2
        self.division=n1/n2
operacion=Calculadora(8,18)
print(operacion.suma)
class Persona:
    edad=17
    altura=1.75
roberto=Persona()
print("La talla es: ",getattr(roberto,'altura'))
print("La talla es: ",roberto.altura)
#ahora como saber si algun objeto tiene alguna propiedad propia de su clase:
print("¿Roberto tiene una edad?",hasattr(roberto,'edad'))
#si se quiere cambiar el valor de alguna propiedad o variable dentro de la clase se utiliza:
setattr(roberto,'edad',18)
print(roberto.edad)
#borrar atributos de un objeto en una clase
#esta funcion trabajo con la clase persona

delattr(Persona,'altura')
print(roberto.edad)
#Metodos a parte del constructorConstructor
class Persona1:
    def __init__(self,nombre,edad,apellido):
        self.nombre=nombre
        self.edad=edad
        self.apellido=apellido
    def descripcion(self,inteligencia):
        self.inteligencia=inteligencia


josue=Persona1("Josue",17,"Sumare")
print("su nombre es",josue.nombre," su apellido: ",josue.apellido," y su edad: ",josue.edad)
josue.descripcion(15)
print(josue.inteligencia)
print("Empieza")
print(josue.descripcion(15))
print("Termina")
#Herencia: se trata de la creacion de una clase a partir de una o mas clases ya existentes
class Pokemon:
    
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo
    def descripcion(self):
        return 'El pokemon se llama {} y es de tipo {}'.format(self.nombre,self.tipo)
class Pikachu(Pokemon):
    def ataque(self,tipodeataque):
        return 'El pokemon pikachu llamado {} tiene un ataque tipo {}'.format(self.nombre,tipodeataque)
class Charmander(Pokemon):
    def ataque(self,tipodeataque):
        return 'El pokemon charmander llamado {} tiene un tipo de ataque {}'.format(self.nombre,tipodeataque)
sebastian=Pikachu("Sebastian","fuego")
print(sebastian.nombre)
print(sebastian.descripcion())
print(sebastian.ataque("rompe colas"))
issai=Charmander("Issai","Fuego")
print(issai.descripcion())
print(issai.ataque("Bola de fuego"))
#Ejercicio herencia complicado
'''class Calculadora:
    def __init__(self,numero):
        self.numero=numero
        self.datos= '''
#Repaso ejercicios profesor 7_12_2020
class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador=numerador
        self.denominador=denominador
    def mostrar(self):
        print(str(self.numerador),"/",str(self.denominador))
pruebadivision=Fraccion(3,4)
pruebadivision.mostrar()
class Perro:
    def __init__(self,tamaño,edad,color,raza):
        self.tamaño=tamaño
        self.edad=edad
        self.color=color
        self.raza=raza
    def descripcion(self):
        print("El perro tiene:\ntamaño: {}\nedad: {}\ncolor: {}\nraza: {}".format(self.tamaño,self.edad,self.color,self.raza))
Pimpon=Perro("Pequeño",4,"marrón","Schnauzer")
Pimpon.descripcion()
class Punto:
    def __init__(self,x,y):
        self.x=x#atributos
        self.y=y
    def imprimir(self):
        print("El punto se ubica en las coordenadas ({},{})".format(self.x,self.y)) 
def main():
    Punto_objeto=Punto(4,8)
    Punto_objeto.imprimir()
main()
'''class Rect:
    def __init__(self,initial_pointx,initial_pointy,ancho,alto):
        self.initial_pointx=initial_pointx
        self.initial_pointy=initial_pointy
        self.ancho=ancho
        self.alto=alto   
def area_rect():
    point=Punto(0,0)
    x=point.coordX
    y=point.coordY
    rect_test=Rect(x,y,4,8)
    print(rect_test.ancho*rect_test.alto)
area_rect()'''

'''class Rect(Punto):
    def descripcion_rectangulo(self,ancho,alto):
        return "El rectangulo tiene:\n1.Punto inicial en:\n-coordenada x en {}\n-coordenada y en {}\n2.Ancho: {}\n3.Alto: {}".format(self.coordX,self.coordY,ancho,alto)
    def punto_central(self):
        return "El punto central es ({},{})".format(self.coordX+(ancho/2),self.coordY+(alto/2))
rectangulo_prueba=Rect(0,0)
print(rectangulo_prueba.descripcion_rectangulo(8,4))
rectangulo_prueba.descripcion_rectangulo(8,4)
print(rectangulo_prueba.punto_central())'''
#ahora la clase sin herencia de punto pero utilizando esta clase
class Rectangulo:
    def __init__(self,ancho,alto,esqx,esqy):
        self.ancho=ancho
        self.alto=alto
        self.esqx=esqx
        self.esqy=esqy
    def medio(self):
        x=self.esqx+(self.ancho/2)
        y=self.esqy+(self.alto/2)
        return (x,y)
def principal():
    punto_esq=Punto(0,0)
    rect_test=Rectangulo(8,4,punto_esq.x,punto_esq.y)
    return rect_test.medio()
print(principal())
class rectangle:
    def __init__(self,ancho,alto,point):
        self.ancho=ancho
        self.alto=alto
        self.point=point
    def descipcion(self):
        print(f"Rectangulo:\n-Ancho: {self.ancho}\n-Alto: {self.alto}\n-Punto inferior izquierdo:({self.point.x},{self.point.y})")        
    def medio(self):
        x=self.point.x+self.ancho/2
        y=self.point.x+self.alto/2
        print(f"El punto medio es: ({x},{y})")
    def punto_izq_inf(self):
        print(f"({self.point.x},{self.point.y})")
    def punto_izq_sup(self):
        a=self.point.y+self.alto
        print(f"El punto A es ({self.point.x},{a})")
    def punto_derecho_inf(self):
        c=self.point.x+self.ancho
        print(f"El punto C es ({c},{self.point.y})")
    def punto_derecho_sup(self):
        d=self.point.x+self.ancho
        e=self.point.y+self.alto
        print(f"El punto B es ({d},{e})")
    def area(self):
        print(f"El area es {self.ancho*self.alto} u2")
def imprimir():
    p=Punto(0,0)
    r=rectangle(4,8,p)
    r.descipcion()
    r.medio()
    r.punto_izq_inf()
    r.punto_izq_sup()
    r.punto_derecho_inf()
    r.punto_derecho_sup()
    r.area()
imprimir()
#Mismidad
p1=Punto(0,4)
p2=Punto(0,4)#mismo contenido. pero difernte objeto(direccion de  memoria)
print(p1==p2)#Es false , ya que es comparan las referencia y no el contenido , esto es diferente al concepto de igualdad profunda
p3=p2#alias
print(p2==p3)
#p4=copy.copy(p2)
#print(p2==p4)
class coordenada:
    def __init__(self,coordx,coordy):
        self.coordx=coordx
        self.coordy=coordy
    def __add__(self,otropunto):#sobrecarga de operadores esto con el fin de sumar dos puntos de coordenadas
        return coordenada((self.coordx+otropunto.coordx),(self.coordy+otropunto.coordy))
        #return(f"({self.coordx+otropunto.coordx} , {self.coordy+otropunto.coordy})")
    def __str__(self,otropunto):
        return(f"-El punto 1 es({self.coordx} , {self.coordy}),\n-El punto 2 es ({otropunto.coordx} , {otropunto.coordy})")
def mostrar():
    coord1=coordenada(4,5)
    coord2=coordenada(10,5)
    #print(coord1.__add__(coord2))
    #coord3=coord1 +coord2
    coord3=coord1.__add__(coord2)
    print(coord3.coordx)
    print(coord3.coordy)
    #print(coord1.__str__(coord2))

mostrar()
class Reloj:
    def __init__(self,hora,minuto,segundo):
        if hora>=12:
            hora%=12
        if minuto>=60:
            hora+=minuto//60
            minuto%=60
            
        if segundo>=60:
            minuto+=segundo//60
            segundo%=60
        self.hora=hora
        self.minuto=minuto
        self.segundo=segundo
    '''def SumarHora(self,otro):
        return Reloj()'''
    #def __add__(self):
    def SumarHora(self,otra_hora):
        hh=self.hora+otra_hora.hora
        mm=self.minuto+otra_hora.minuto
        ss=self.segundo+otra_hora.segundo
        a=Reloj(hh,mm,ss)
        return f"La suma de ambas horas es {a.mostrar()}"
    def mostrar(self):
        return f"La hora es {self.hora} con {self.minuto} minutos y {self.segundo} segundos"
    def convertirSegundos(self):
        return f"Los segundos son {self.hora*3600+self.minuto*60+self.segundo}"

    '''def convertirSegundos(self):
        if self.segundo>=60 and self.segundo<3600:
            self.segundo%=60
        return self.segundo
        if self.segundo>=60:
            self.segundo=self.segundo%60
            self.minuto=self.minuto+self.segundo//60
        if self.minuto>=60:
            self.minuto=self.minuto%60
            self.hora=self.hora+self.minuto//60
        return Reloj(self.hora,self.minuto,self.segundo)'''
def printear():
    reloj=Reloj(2,129,80)
    reloj2=Reloj(3,20,0)
    print(reloj.convertirSegundos())
    print(reloj.mostrar())
    print(reloj.SumarHora(reloj2))
printear()
#Herencia clase
import math
print(math.log  (4))
