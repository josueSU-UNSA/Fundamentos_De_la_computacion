#Busqueda lineal :
def busqueda_lineal(lista,elemento):
    if elemento in lista:
        for i,v in enumerate(lista):
            if v ==elemento:
                return i
    else:
        return "El elemento a buscar no se encuentra en el arreglo "    
lista1=["buenos","dias","hola"]
#print("El indice del lemento a buscar es: "+str(busqueda_lineal(lista1,"hola")))

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return "El elemento no se encontro"
#print(search_linear(lista1,"jaja"))
def buscar_elemento(lista,elemento):
    for (i,palabra) in enumerate (lista):
        if palabra==elemento:
            return i
    return -1

def palabras_desconocidas(texto,vocabulario):
    palabras_sin_conocer=[]
    texto=texto.split()
    for i in texto:
        if (buscar_elemento(vocabulario,i)==-1):
            palabras_sin_conocer.append(i)
    return palabras_sin_conocer
text="Hubo una vez un rey que tenía un gran palacio cuyos jardines eran realmente maravillosos"
vocab = ["vez", "rey", "gran", "un","jardines", "chica","el", "arbol"]
print(palabras_desconocidas(text,vocab))
