#Busqueda lineal
def busqueda_lineal(numero,lista):#Definimos la funcion de busqueda lineal
    if numero in lista:#la primera condicion que debe cumplir para hacer la busqueda es que el elemento este en la lista 
        for i in range(len(lista)):#realizamos un bucle que comparara los valores
            if lista[i] == numero:#si el valor de la lista es igual que el del elemento
                respuesta=i#creamos una variable respuesta que mas adelante se retornara
        return respuesta#retornamos como respuesta el indice del ultimo elemento encontrado
    else:#de no estar el elemento en la lista pues no se realizara el bucle comparativo y por lo tanto retornara un falso que significara que el elemento no se encuentra en la lista
        return False 
numeros=[2,8,30,4,5]
print(busqueda_lineal(30,numeros))
#Busqueda binaria recursiva
def busqueda_binaria_recursiva(elemento,lista,i_inicio,i_final):#definimos la lista con dos parametros extras que seran nuestra ayuda al entrar al caso recursivo
    i_medio=(i_final+i_inicio)//2#definimos a la posicion del medio como la division entera de la posisicon del primer elemento con el segundo esto se renovara con cada recursion 
    if lista[i_medio]==elemento:#si el elemento del medio es el eelemento a buscar pues se encontro el elemnto 
        return i_medio
    elif elemento>lista[i_medio]:#de lo contrario ser mayor entonces se buscara en la parte de menores
        return busqueda_binaria_recursiva(elemento,lista,i_medio+1,i_final)#funcion se cambia el final por la posicion media menos 1 esto para buscar en los menores y viceversa
    else:
        return busqueda_binaria_recursiva(elemento,lista,i_inicio,i_medio-1)

lista_auxiliar=[15,17,20,30,40]
print(busqueda_binaria_recursiva(30,lista_auxiliar,0,len(lista_auxiliar)-1))

#Ordenamiento por insercion
def ordenamientoPorInsercion(lista):#definimos la funcion ordenamiento por insercion
    for i in range(1,len(lista)):#vamos desde el el termino numero dos esto para poder comparar el termino anterior
        valoractual = lista[i]#definimos una variable la cual sera el elemento  en si que se empieza a comparar
        posicion = i#esta variable posicion es necesaria para buscar el elemento anterior a la variable valor actual
        while lista[posicion-1]>valoractual and posicion>0 :#entrara al bucle a hacer el procedimiento de intercambio siempre y cuando el valor anterior al valor en este caso que empieza en el segunda definindo en el bucle anterior y si la posicion es mayor que cero , ya que de nos ser mayor que cero haria habria un indice no valido para el valor o uno negativa que haria que la funcion compare el primero con el ultimo termino
            lista[posicion]=lista[posicion-1]#de cumplirse estos requisitos se hara un ordenamiento in place en el cual la posicion que se asigna que en este caso empieza en el segundo se iguale al primero ya que este es mayor
            posicion = posicion-1#mientras que la posicion retrocedera en uno para seguir comparando el anterior valor para que si este es menor que el anterior siga bajando
        lista[posicion]=valoractual#esta nueva posicion sera la nueva variable valor actual que se comparara en el bucle while para ver si es menor que la posicion a la izquierda de este
    return lista#retorna la lista ordenada

unaLista = [54,26,93,17,77,31,44,55,20]
print(ordenamientoPorInsercion(unaLista))
#Ordenamiento quicksort recursivo
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
print(quicksort(unaLista))