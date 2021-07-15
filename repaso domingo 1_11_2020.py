#OJO SI QUIERES PROBAR CADA UNA DE LAS FUNCIONES ENTONCES TIENES QUE QUITAR LA ETIQUETA DE COMENTARIOS QUE TIENEN LOS  INPUT Y PRINT DE PRUEBA DE CADA FUNCIÓN
# Nª1 primera parte funcion que introduzco el numero del dia y me da nombre
def day_name (i):
    dias_de_la_semana=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    if 0<=i<len(dias_de_la_semana):
        return dias_de_la_semana[i]
    mensaje_de_atencion="¡¡¡Porfavor introduce solamente un valor de 0 a 6!!!"
    return mensaje_de_atencion.upper()
    
#x=int(input("Introduce un número del 0 a 6 el cual se relacione con los numeros del día de la semana recuerda que 0 es domingo: "))
#print(day_name(x))
# Nª2 segunda parte funcion que me pide un punto cardinal y te bota la siguiente
def clockwise(cardinalpoint):
    cardinalpoint= cardinalpoint.lower()
    points_cardinals =["north","west","south","east"]
    for i in range(len(points_cardinals)):
        if cardinalpoint == points_cardinals[i]:
            return points_cardinals[(i+1)%4]
#punto_cardinal_de_prueba=input("Escriba cualquiera de estos puntos cardinales y le retornaremos el siguiente punto cardinal en orden antihorario:\n1.North\n2.West\n3.South\n4.East\nIntroduce un punto cardinal de la lista: ")
#print(clockwise(punto_cardinal_de_prueba))
# Nª3 tercera parte me pide un dia de la semana y tengo que retornar el numero de orden que ocupa la semana claro de 0 a 6
def day_num(day):
    day =day.lower()
    days_of_the_week=["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
    for i in range (len(days_of_the_week)):
        if day==days_of_the_week[i]:
            return i
#dia=input("Introduce el dia de la semana que deseas saber que orden tiene: ")
#print(day_num(dia))        
# Nª4 cuarta parte funcion en la cual tengo que introducir un dia  y los dias que se estara fuera de casa y devolver el dia que se regresara 
def day_add(day,days_out_of_home):
    day = day_num(day)
    day_that_coming_of_my_our_home=(day+days_out_of_home)%7
    result=day_name(day_that_coming_of_my_our_home)
    return result
#dia_auxiliar=input("Introduce el dia que saldras: ")
#dias_fuera_de_casa_auxiliar=int(input("Introduce la cantidad de días que estaras fuera de casa: "))
#print(day_add(dia_auxiliar,dias_fuera_de_casa_auxiliar))
# Nª5 quinta pregunta es la cuarta pero con dias que se estara afuera negativo
#dia_auxiliar=input("Introduce el dia que saldras: ")
#dias_fuera_de_casa_auxiliar=int(input("Introduce la cantidad de días que estaras fuera de casa: "))
#print(day_add(dia_auxiliar,dias_fuera_de_casa_auxiliar))
# Nª6 sexta pregunta en la que me pide un mes y que me bote la cantidad de dias que tiene este mes
def days_in_month(mes):
    mes=mes.lower()
    mesesde30=["abri","junio","setiembre","noviembre"]
    for i in mesesde30:
        if mes == i:
            return 30
        elif mes=="febrero":
            return "28 en un año normal y 29 en un año bisiesto"
        return 31
#mes_auxiliar=input("introduzca el mes que necesita saber la cantidad de días que tiene: ")
#print(days_in_month(mes_auxiliar))
# Nª16 en el que ponga un divisor y su dividendo siendo esta una division exacta botandome el valor de verdad
def is_factor(divisor,dividendo):
    if dividendo%divisor==0:
        return True
    return False
#divisor_de_prueba=int(input("Introduce el divisor que utilizaras: "))
#dividendo_de_prueba=int(input("Introduce el dividendo de prueba que utilizaras: "))
#print(is_factor(divisor_de_prueba,dividendo_de_prueba))
# Nª17 funcion que me pida un dividendo y un divisor en ese orden y que me entregue si la relacion antes mencionada en ese orden es correcta
def is_multiple(dividendo1,divisor1):
    if is_factor(divisor1,dividendo1)==True:
        return True
    return False
#dividendo_de_prueba=int(input("Introduce el dividendo de prueba que utilizaras: "))
#divisor_de_prueba=int(input("Introduce el divisor que utilizaras: "))
#print(is_multiple(dividendo_de_prueba,divisor_de_prueba))
#funcion que calcule el factorial de un numero
def factorial(n):#una funcion factorial
    factorialn=1
    for i in range(1,n+1):
        factorialn=factorialn*i
    return factorialn
print(factorial(0))
#recursividad es cuando una funcion se llama a si misma
#toda recursividad debe de tener un punto de parada (caso base el cual detiene el bucle)
def factorial_recursivo(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursivo(n-1)
print(factorial_recursivo(5))
#haciendo fibonacci con una funcion recursiva
def fibo(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(6))
#implementando una funcion recursiva que imprime numeros del 5 al 1
def print_num(n):
    if n==0:
        return
    print(n)
    print_num(n-1)
print_num(5)

# -*- coding: UTF-8 -*-
 
# función para el calculo de pascal
# tiene que recibir el numero de lineas que tendra
def trianguloPascal(n):
 
    # creamos una lista que contendra los dos primeras lineas
    lista = [[1],[1,1]]
 
    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):
 
        # inicializamos la linea
        linea = [1]
 
        # bucle por cada uno de los valores de la anterior linea
        for j in range(0,len(lista[i])-1):
 
            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            linea.extend([ lista[i][j] + lista[i][j+1] ])
 
        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        linea += [1]
 
        # añadimos la linea a la lista
        lista.append(linea)
 
    #devolvemos la lista ya creada
    return lista
 
try:
    n = int(raw_input("Numero de lineas para triangulo de Pascal: "))
    resultado = trianguloPascal(n)
 
    # mostramos el resultado
    for i in resultado:
        print (i)

except:
    print ("\nTiene que ser un valor numerico")
print(trianguloPascal(5))

