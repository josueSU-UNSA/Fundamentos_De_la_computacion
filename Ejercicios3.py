import sys 
def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)
#3 funcion add_vectors,escalar_mult, dot_product
def sumar_lista(lista):#funcion auxiliar que me permitira sumar la lista en la ultima funcion
    count=0#contador en 0
    for i in lista:#iteramos los valores de la lista
        count+=i#agregamos los valores de la lista al contador para asi sumarlos
    return count#retornamos el contador es decir la suma de todos los valores de la lista

def add_vectors(lista1,lista2):#definimos la primera funcion
    new_list=[]#utilizamos una lista vacia en la que agregaremos los valores que nos retorna nuestra funcion
    if len(lista1)!=len(lista2):#ponemos la condicion de que la longitud de las listas deben ser las mismas de lo contrario no se podra realizar la operacion
        print("no se puede realizar la operacion con listas de diferentes longitudes")#imprimos en pantalla el mensaje de no cumplir con la condicion que tengan misma longitud
    else:
        for i in range (len(lista1)):#ponemos una iteracion para despues utilizar estos valores como indices de las operaciones de las listas
            new_list.append(lista1[i]+lista2[i])#agregamos a la lista vacia la suma de los valores con el mismo indice a la lista
        return new_list#al final despues de realiza todas las operaciones retornamos nuestra lista vacia en este caso llena por las operaciones realizadaas
print(add_vectors([1,1],[1,1]))
def escalar_mult(numero_escalar,lista):#definimos la segunda funcion pedida 
    new_list=[]#creamos una lista vacia
    for i in lista:#itermaos los valores de la lista
        new_list.append(numero_escalar*i)#al iterar esos valores cada uno lo multiplicamos por el valor escalar que deseamos
    return new_list#retornamos las lista con la multiplicacion de los valores de la lista con el valor esclar 
print(escalar_mult(4,[5,6,7]))
def dot_product(lista1,lista2):#defininmos la funcion pedida
    new_list=[]#creamos una lista vacia
    for i in range(len(lista1)):#iteramos los indices de la lista suponiendo que ambas listas tienen igual longitud
        new_list.append(lista1[i]*lista2[i])#agregamos la multiplicacion de los valores de la lista que tienen el mismo indice ya que esa es la operacion a realizar para resolver el problema a la lista vacia
    return sumar_lista(new_list)#al final retornamos la suma de las listas teniendo como apoyo la funcion def sumar_lista para retornar la suma de la lista que armamos 
print(dot_product([1,2],[1,5]))
def test_suite():
    test(add_vectors([1, 1], [1, 1]), [2, 2])#test para la funcion add_vectors
    test(add_vectors([1, 2], [1, 4]), [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]), [2, 6, 4])
    test(escalar_mult(2, [1, 1]), [2, 2])#test para la funcion de multiplicacion escalar
    test(escalar_mult(4, [1, 4]), [4,16])
    test(escalar_mult(3, [2, 4, 3]), [6, 12, 9])
    test(dot_product([1, 1], [1, 1]),2)#test para la funcion dot product
    test(dot_product([1, 2], [1, 4]), 9)
    test(dot_product([1, 2, 1], [1, 4, 3]), 12)
test_suite()