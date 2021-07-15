class Punto:#se crea la clase punto
    def __init__(self,coordenadax,coordenaday):#se desarrolla el metodo constrcutor con los atributos coordenadax y coordenaday
        self.coordenadax=coordenadax
        self.coordenaday=coordenaday
    def __str__(self):#El metodo __str__ nos permite transformar en este caso un objeto punto en una cadena que me imprima las coordenadas que posee este objeto de clase Punto
        return f"({self.coordenadax} , {self.coordenaday})"
    def __add__(self,other):#El metodo __add__ nos permite sobrecargar una suma de objetos que sean de clase Punto
        return Punto(self.coordenadax+other.coordenadax,self.coordenaday+other.coordenaday)#nos devuelve en este caso un objeto de clase punto esto con el fin de mas adelante sea una instancia e imprimirlo con el metodo anterior __str__
#pregunta2
def agregar_lista(elemento,lista):#creamos una funcion para agregar el elemento respectivo a la lista que le corresponde tanto si es de las coordenas x se le agregara a la lista de x y siu es de coordenada y se le agregara a la lista y
    lista.append(elemento)#se agrega a  la lista respectiva
def buble_sort(lista):#utilizamos el ordenamiento de burbuja , ordenamiento cuyo nombre viene porque asemeja el comportamiento de las burbujas en una bebida , ya que al igual que las burbujas se posicionan encima o arriba de la bebida , este metodo lo que hace es hallar primero los vlaores maximos 
    for j in range(len(lista)-1):#hace el recorrido general para la lista
        for i in range(len(lista)-1):#este es el bucle encargado de hallar los maximos
            a=lista[i+1]#varibale que se utilizara para hacer los respectivos reemplazos
            if lista[i+1]<lista[i]:#si el elemento siguiente es menor que el actual entonces se procede a hacer el intercambio
                lista[i+1]=lista[i]#el elemento siguiente ahora sera el mayor
                lista[i]=a#el elelemento que era el mayor se volvera el menor
                #y de esta manera se efectuo el cambio
    return lista#retorna la lista ordenada

listax=[]#se crea una lista para ordenar a las coordenadas x
listay=[]#se crea una lista para ordenar a las coordenas y
#se crean las instancias
p1=Punto(3,1)
p2=Punto(0,2)
p3=Punto(2,3)
p4=Punto(1,4)
p5=Punto(-1,6)
#utilizamos la funcion para agregar los elementos a la lista correspondiente
agregar_lista(p1.coordenadax,listax)
agregar_lista(p2.coordenadax,listax)
agregar_lista(p3.coordenadax,listax)
agregar_lista(p4.coordenadax,listax)
agregar_lista(p5.coordenadax,listax)
agregar_lista(p1.coordenaday,listay)
agregar_lista(p2.coordenaday,listay)
agregar_lista(p3.coordenaday,listay)
agregar_lista(p4.coordenaday,listay)
agregar_lista(p5.coordenaday,listay)
#imprimimoos para que en pantalla se pueda ver los resultados del ordenamiento de las listas
print(f"La lista de las coordenadas x en orden es {buble_sort(listax)}")
print(f"La lista de las coordenadas y en orden es {buble_sort(listay)}")