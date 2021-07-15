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
#4 Funcion recursiva para sumar los elementos de una lista de enteros
def suma_recusiva(lista):#funcion suma recursiva
    if len(lista)==1:#definimos el caso base el cual sera que el largo de esta lista sea 1 esto con un proposito que pasara a ser explicado en las siguientes lineas
        return lista[0]#de darse este caso me arroja el unico valor de la lista
    else:
        return lista[0]+suma_recusiva(lista[1:])#caso recursivo: lo que hacer es sumarme primero el primer valor de la lista para despues tomar otro fragmentos de la lista el cual sera el segundo valor de esta para que la funcion evalue si es de largo 1 entonces se sumara solo con el segundo elemento de lo contrario seguira suma el primer indice pero del fragmento de lista que se saco anteriormente con el fin de que al llegar a este ser de longitud 1 solo se sume ese valor mas lo cual entraria en el caso base 
def test_suite():
    test(suma_recusiva([1, 1, 1]),3)
    test(suma_recusiva([1,2,4]),7)
    test(suma_recusiva([2,14,3,7]),26)
test_suite()