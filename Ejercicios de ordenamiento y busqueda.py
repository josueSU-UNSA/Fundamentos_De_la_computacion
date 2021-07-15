#Busqueda
def lineal_search(lista,elemento):
    for (i,j) in enumerate(lista):
        if j==elemento:
            return i
    return -1
#UN problema mas realista
def encontrar_palabras_desconocidas(texto,vocabulario):
    palabras_desconocidas=[]
    texto=texto.split()
    for i in texto:
        if (lineal_search(vocabulario,i)==-1):
            palabras_desconocidas.append(i)
    return palabras_desconocidas
texto_ayuda='''Hola banana soy yo denuevo tu amigo la fresa'''
vocabulario=["banana"]
print(encontrar_palabras_desconocidas(texto_ayuda,vocabulario))
def busqueda_binaria_re(lista,elemento,inicio,fin):
    medio=(inicio+fin)//2
    if lista[medio]==elemento:
        return medio
    elif elemento>lista[medio]:
        return busqueda_binaria_re(lista,elemento,medio+1,fin)
    else:
        return busqueda_binaria_re(lista,elemento,inicio,medio-1)
lista3=[7,59,60,120,180]
print(busqueda_binaria_re(lista3,180,0,len(lista3)-1))
def buble_sort(lista):#ordedna encontrando primero los elementos menores
    for j in range(len(lista)-1):
        
        for i in range(len(lista)-1):
            reemplazar=lista[i]
            if lista[i]>lista[i+1]:
                lista[i]=lista[i+1]
                lista[i+1]=reemplazar
    return lista
print(buble_sort([78,89,90,6,5,4,48,32,26,140]))
def selection_sort(lista):#ordena primero encontrando los elementos menores o minimos
    for i in range(len(lista)-1):
        pos_min=i
        for j in range(i+1,len(lista)-1):
            if lista[j]<lista[pos_min]:
                pos_min=j
        if pos_min !=i:
            variable_para_intercambio=lista[i]
            lista[i]=lista[pos_min]
            lista[pos_min]=variable_para_intercambio
    return lista
print(selection_sort([78,89,90,6,5,4,48,32,26,140]))
def insercion(lista):
    for i in range(1,len(lista)):#vamos desde el el termino numero dos esto para poder comparar el termino anterior
        valoractual = lista[i]#definimos una variable la cual sera el elemento  en si que se empieza a comparar
        posicion = i#esta variable posicion es necesaria para buscar el elemento anterior a la variable valor actual
        while lista[posicion-1]>valoractual and posicion>0 :#entrara al bucle a hacer el procedimiento de intercambio siempre y cuando el valor anterior al valor en este caso que empieza en el segunda definindo en el bucle anterior y si la posicion es mayor que cero , ya que de nos ser mayor que cero haria habria un indice no valido para el valor o uno negativa que haria que la funcion compare el primero con el ultimo termino
            lista[posicion]=lista[posicion-1]#de cumplirse estos requisitos se hara un ordenamiento in place en el cual la posicion que se asigna que en este caso empieza en el segundo se iguale al primero ya que este es mayor
            posicion = posicion-1#mientras que la posicion retrocedera en uno para seguir comparando el anterior valor para que si este es menor que el anterior siga bajando
        lista[posicion]=valoractual#esta nueva posicion sera la nueva variable valor actual que se comparara en el bucle while para ver si es menor que la posicion a la izquierda de este
    return lista#retorna la lista ordenada
    
            
