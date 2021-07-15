 w#POO
#Es algo con propiedades y comportamiento
#perro 
# Propiedades o atributos del peroo:tamaño edad color raza
#Comportamientos o metodos: caminar,ladrar,saltar.dormir
#clase estructura general del obejto
#Instancia varibales creadas a partir de la clase ejm: pimpom=perro(marron,macho,negro)
#clase es plantilla general del objeto
class perro:
    def __init__(self,tamaño,edad,color,raza):
        self.tamaño=tamaño
        self.edad=edad
        self.color=color
        self.raza=raza
    def mostrar(self):
        print("mide {} tiene {} años de edad su color es {} y es de raza {}".format(self.tamaño,self.edad,self.color,self.raza))

negro=perro(3,4,"negro","rotweiler")
negro.mostrar()
class rectangulo:
    def __init__(self,x,y,ancho,alto):
        self.x =x
        self.y =y
        self.ancho =ancho
        self.alto =alto
    def area(self):
        print("El area del rectangulo ubicado en el punto del eje x: {} y en ele ejer y: {} con ancho: {} y alto: {} tiene el area: {}".format(self.x,self.y, self.ancho ,self.alto ,self.ancho*self.alto))
rect=rectangulo(0,0,8,5)
rect.area()
class rectmedio:
    def __init__(self,x,y,ancho,alto):
        
        self.x=x
        self.y=y
        self.ancho=ancho
        self.alto=alto
    def mostrar(self):
        print("El centro del rectangulo cuya esquina inferior izquierda se ubica en el eje de ordenadas: {} y el eje de abscisas: {} con ancho: {} y alto: {} tiene un area: {} ".format(self.x,self.y,self.ancho,self.alto,(self.x+self.ancho/2,self.y+self.alto/2)))
prueba=rectmedio(0,0,4,8)
prueba.mostrar()
#Herencia