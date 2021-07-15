#pregunta 4 examen
def is_even(n):
    if n%2==0:
        return True
    return False
def count_evens(list):#se implementa un contador
    n=0
    for i in list:
        if is_even(i) is True:
            n+=1
    return n
a=[2,4,5,6,8]
print(count_evens(a))
#pregunta 5 examen
def count_sub_cadenas(cadena,subcadena):
    con=0
    for i in range(len(cadena) - len(subcadena) +1):
        apoyo=""
        for ii in range (len(subcadena)):
            apoyo+=cadena[ii+i]
        if subcadena==apoyo:
            con+=1
        return con
oracion="una laguna en el Coropuna"
palabra = "una"
print(count_sub_cadenas(oracion,palabra))
#pregunta 6 examen
def es_primo(num):
    for i in range(2,num):#Asumiendo que se ingresa numeros enteros postivos
        if num%i==0:
            return False
    return True
def contar_primos(lista):
    n=0
    for i in lista:
        if es_primo(i) is True:
            n+=1
    return n

print(contar_primos([2,5,7,13,4,8]))