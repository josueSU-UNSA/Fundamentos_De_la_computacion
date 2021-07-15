#pregunta 1
class Punto:#se crea la clase punto
    def __init__(self,coordenadax,coordenaday):#se desarrolla el metodo constrcutor con los atributos coordenadax y coordenaday
        self.coordenadax=coordenadax
        self.coordenaday=coordenaday
    def __str__(self):#El metodo __str__ nos permite transformar en este caso un objeto punto en una cadena que me imprima las coordenadas que posee este objeto de clase Punto
        return f"({self.coordenadax} , {self.coordenaday})"
    def __add__(self,other):#El metodo __add__ nos permite sobrecargar una suma de objetos que sean de clase Punto
        return Punto(self.coordenadax+other.coordenadax,self.coordenaday+other.coordenaday)#nos devuelve en este caso un objeto de clase punto esto con el fin de mas adelante sea una instancia e imprimirlo con el metodo anterior __str__
    def distancia(self,otro_punto):#definimos una metodo que calcule al distancia entre puntos
        return (((self.coordenadax-otro_punto.coordenadax)**2)+((self.coordenaday-otro_punto.coordenaday)**2))**0.5
def imprimir():#creamos una funcion que no recibira parametros ,pero que nos permitira visualizar las acciones que realizan los metodos de la clase punto
    p=Punto(3,5)#se crea una instancia de clase Punto con atributos que seran las coordenadas
    q=Punto(6,8)#se crea una instancia de clase Punto con atributos que seran las coordenadas
    r=p+q#en si esta es la sobrecarga de operadores que algunos lenguajes permiten en este caso python que te permite realizar operaciones con diferentes objetos ,pero la operacion a realziar segun el signo debe estar indicada como un metodo en este caso el metodo __add__
    print(r)#imprimir este objeto de clase Punto o instancia tambien por asi decirlo se sobrecagra un operador en este caso el metodo __str__ que te permite imprimir un objeto en pantalla pero en si lo que hace es imprimir las coordenadas en forma de cadena
imprimir()#se invoca a la funcion para poder ver los resultados en el terminal



