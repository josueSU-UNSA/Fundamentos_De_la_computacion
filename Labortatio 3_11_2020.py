cadena="Hola mundo"
letra=cadena[3]
letra =letra.upper()
print(letra)
print(cadena[:4])
print(cadena[4:])
print("a"<="z")#ojo es en orden alfabeto toman valores y siempre las minusculas son menores que las mayusculas, pero no es el valor del alfabeto , sino del numero que le pertenece en ascii 
#implementar un algoritmo que permita encontrar una letra en una cadena
'''def find_caracter(cadena,letra):
    for i in range(len(cadena)):
        if cadena[i] ==letra:
            return True
print(find_caracter("hola hoy","h"))'''
#encontrar el numero de ocurrencias en una cadena
def find_caracter_contador(cadena,letra):
    contador=0
    for i in range(len(cadena)):
        if cadena[i] ==letra:
            contador+=1
    return contador
print(find_caracter_contador("hola hoy","h"))
#ahora con while
'''def find_caracter(cadena,letra):
    
    i=0
    while i <len(cadena):
        if cadena[i] ==letra:
            print("se encontró",indice)
            break
        indice+=1
    if indice==len(cad)    
print(find_caracter("hola hoy","h"))'''
#con un bucle while