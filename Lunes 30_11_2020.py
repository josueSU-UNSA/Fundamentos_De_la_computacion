'''Algoritmos de ordenamiento'''
# Burbuja-bubble sort
#se repite el largo de la lista-1
#Se agrupan de dos en dos y el mayor se mueve a la derecha, entonces en general se encuentran primero los mayores
#es n**2
def bubbleSort(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
    return lista
print(bubbleSort([9,8,7,6,5,4,3,2,1]))
#seleccion-selection sort
#se busca siempre los minimos es decir va avanzando de manera que se ordenan primero los numeros mas pequeños
#es n**2
def selectionSort(lista):
    for i in range(len(lista)):
        posicion_del_minimo=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[posicion_del_minimo]:
                posicion_del_minimo=j
        if posicion_del_minimo!=i:
            temp =lista[i]
            lista[i]=lista[posicion_del_minimo]
            lista[posicion_del_minimo]=temp
    return lista 
#insersion-insertion sort aprender esto muy importante
#lo que pasa es que se ordena siempre de manera ordenada desde menores a mayores pero siempre comparando si el de la izquierda es mayor
#En el peor caso es n**2 en el mejor es n
def ordenamientoPorInsercion(unaLista):
    for i in range(1,len(unaLista)):
        valorActual = unaLista[i]
        posicion = i
        while posicion>0 and unaLista[posicion-1]>valorActual:
            unaLista[posicion]=unaLista[posicion-1]
            posicion = posicion-1
            unaLista[posicion]=valorActual
    return unaLista

unaLista = [54,26,93,17,77,31,44,55,20]
print(ordenamientoPorInsercion(unaLista))
#Quick sort importante aprender esto
#manera iterativa complejidad n log n en el peor caso n**2
#def quicksort_profesor(lista):

#Radix sort
#Merge sort
'''Algoritmo de busqueda'''
#busqueda Lineal de uno a uno no necesariamente ordenada y tampoco elementos de la lista repetidos
#Tarea
numeros=[0,1,2,3,4,5,6,7,8,9]
def busqueda_lineal(numero,lista):
    if numero in lista:
        for i in range(len(lista)):
            if lista[i] == numero:
                respuesta=i+1
        return respuesta
    else:
        return False 
print(busqueda_lineal(30,numeros))
#busqueda binaria tiene que estar una lista ordenada
#numero de pasos en busqueda binaria numero_de_pasos=log2(largo de la lista)=log 2 (n)

def busqueda_binaria(a,num):
    i_inicio=0
    i_final=len(a)-1
    while i_inicio<=i_final:
        i_medio=i_inicio+(i_final-i_inicio)//2
        valor_medio=a[i_medio]
        if valor_medio==num:
            return i_medio
        elif num<valor_medio:
            i_final=i_medio-1
        else:
            i_inicio=i_medio+1
    return None
print("Aca empieza")
print(busqueda_binaria([9,10,7,6,8,3,88,76,54,32,15],88))
print("aca termina")
#Analisis de algorimtos
#complejidad
lista1=[i for i in range(8)]
print(lista1)
lista2=[12,34,56,78,99]
for j in range(len(lista2)-1):
    lista2[j]
#print(lista2[j+1])
#ordenar la lista con buble sort
def buble_sort_2(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                variable_ayuda=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=variable_ayuda
    return lista
print(buble_sort_2([5,9,7,6,8,4,2,3,1])) 
print(selectionSort([5,9,7,6,8,4,2,3,1]))
#Tarea
#1 Insertion sort
'''def ordenamientoPorInsercion(unaLista):
    for i in range(1,len(unaLista)):
        valorActual = unaLista[i]
        posicion = i
        while posicion>0 and unaLista[posicion-1]>valorActual:
            unaLista[posicion]=unaLista[posicion-1]
            posicion = posicion-1
            unaLista[posicion]=valorActual
    return unaLista'''

unaLista = [54,26,93,17,77,31,44,55,20]
#print(ordenamientoPorInsercion(unaLista))
#print(unaLista)
#Algoritmo quick sort recursivo
def particionando(lista):
    pivote=lista[0]
    menores=[]
    mayores=[]
    for i in range(1,len(lista)):
        if lista[i]<pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return (menores , pivote , mayores)
def quicksort(lista):
    if len(lista)<2:
        return lista
    (menores,pivote,mayores)=particionando(lista)
    return quicksort(menores)+[pivote]+quicksort(mayores)
print(quicksort(unaLista))
#algortimo de busqueda binaria recursivo
def busqueda_binaria_recursiva(elemento,lista,i_inicio,i_final):
    if i_inicio>i_final:
        return None
    
    i_medio=(i_final-i_inicio)//2
    
    if lista[i_medio]==elemento:
        return i_medio
    elif lista[i_medio]>elemento:
        return busqueda_binaria_recursiva(lista,elemento,i_inicio,i_medio-1)
    else:
        return busqueda_binaria_recursiva(lista,elemento,i_medio+1,i_final)
lista1=[54,26,93,17,77,31,44,55,20]
#print(busqueda_binaria_recursiva(lista1,26,0,len(lista1)-1))

