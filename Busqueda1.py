def busqueda_binaria(lista,elemento):
    i_inicio=0
    i_final=len(lista)-1
    while i_inicio<=i_final:
        i_medio =(i_inicio+i_final)//2
        if lista[i_medio]==elemento:
            return i_medio
        elif elemento<lista[i_medio]:
            i_final=i_medio-1
        #if elemento>i_medio:
        else:
            i_inicio=i_medio+1
print(busqueda_binaria([10,50,80,80,85,90,140,170,200],90)) 
def binaria_recursiva(lista,elemento,inicio,final):
    i_medio=(inicio+final)//2
    if lista[i_medio]==elemento:
        return i_medio
    elif elemento<lista[i_medio]:
        return binaria_recursiva(lista,elemento,inicio,i_medio-1)
    else:
        return binaria_recursiva(lista,elemento,i_medio+1,final)
lista=[10,50,80,80,85,90,140,170,200]
print(binaria_recursiva(lista,170,0,len(lista)-1)) 
def busqueda_lineal_re(lista,elemento,indice):
    #indice=0
    if lista[indice]==elemento:
        return indice
    else:
        return busqueda_lineal_re(lista,elemento,indice+1)
lista2=[80,15,470,90,5,4,756]
print(busqueda_lineal_re(lista2,5,0)) 
#Algorimtos de ordenamineto:
# Algoritmo de ordenamiento Buble sort:
def buble_sort(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            a=lista[i+1]
            if lista[i+1]<lista[i]:
                lista[i+1]=lista[i]
                lista[i]=a
    return lista
print(buble_sort([80,15,470,90,5,4,756,500,79,40]))#En este metodo se encuentran primero los numeros que sean mayores se llama buble sort , ya que simula el comportamiento de las burbujas , que lo que hacen es se posicionan encimaa de las bebidas
#Ordenamiento por seleccion
def seleccion_sort(lista):#se encuentran los elementos minimos
    for i in range(len(lista)):
        posisicion_minimo=i
        for j in range (i+1,len(lista)):
            if lista[j]<lista[posisicion_minimo]:
                posisicion_minimo=j
        if posisicion_minimo!=i:
            intercambiar=lista[i]
            lista[i]=lista[posisicion_minimo]
            lista[posisicion_minimo]=intercambiar
    return lista
print(seleccion_sort([80,15,470,90,5,4,756,500,79,40]))#se ordena primero los primeros elemeneots   
#Ordenamineto por insercion:mas eficeinte que seleccion
def ordenPorInsercion(lista): #se ordenan conforme avanzan
    for i in range(1,len(lista)):
        actual=lista[i]
        indice=i
        while indice>0 and lista[indice-1]>actual:#va retrocediendo hasta encontrar un elemento menor o hasta llegar a la primera posicion si fuese este el menor de todos
            lista[indice]=lista[indice-1]
            indice=indice-1
        lista[indice]=actual
    return lista
print(ordenPorInsercion([80,15,470,90,5,4,756,500,79,40]))
#Ordenamiento quick sort
def particionando(lista):# Definmos una funcion auxiliar para separar en las 3 partes que nos pide la quicksort que en este caso es un pivote , los menores , los mayores
    pivote=lista[0]#Se escoje como pivote por defecto al primer elemento lista
    menores=[]#Se crea una lista auxiliar que sean los menores que iran mas adelante a la izquierda del pivote
    mayores=[]#Se crea otra lista auxiliar que sean los mayores que estaran a la derecha del pivote
    for i in range(1,len(lista)):#Se pone como un range empezando del segundo elemento , ya que el primer elemento sera el pivote
        if lista[i]<pivote:#Si el elemento desde el segundo al ultimo hay un elemento menor que el pivote este se agregara a la lista menores
            menores.append(lista[i])#Se agrega el elemento menor a la lista menores del pivote
        else:
            mayores.append(lista[i])#Al no cumplirse que sea menor que el pivote se agregara a la lista auxiliar mayores
    return (menores , pivote , mayores)#lo que retorna son una tupla con la lista menores , pivote y mayores
def quicksort(lista):#Se define la funcion recursiva quicksort
    if len(lista)<2:#Si el largo de la lista es menor a 2 quiere decir que la lista ya esta ordenada o que solo hay
        return lista #El caso base sera este ya que lo que pasara esque si la lista se encoge conforme las dentro de las listas se van conformando sublistas al tener un largo menor que dos quiere decir que ya no se puede hacer nada mas ya que esa parte esta ordenada
    else: #caso contrario entra al caso recursivo
        (menores,pivote,mayores)=particionando(lista)#En este caso se iguala tres variables dentro de una tupla a los valores que tambien estan dentro de una tupla que sera el retorno de la funcion particionando pero en este caso lo que se particionara sera la lista para asi elegir el pivote , los menores y mayores 
        return quicksort(menores)+[pivote]+quicksort(mayores)#el caso se repetira para las listas menores y mayores , ya que el unico valor fijo sera el pivote que en este caso sera el pivote de no habre menores que el pivote solo se hara el caso recursivo para los mayores y vicevera
print(quicksort([80,15,470,90,5,4,756,500,79,40]))


    


