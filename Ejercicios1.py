import sys 
def test(actual, expected):#definimos la funcion test
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
#1 Eliminar apariciones de una subacadena
def remove_all(sub_cadena,cadena):
    cad=cadena.split(sub_cadena)#lo que hace esta parte es que la cadena se divide en una lista al encontrar el separador sub_cadena lo que de paso lo elimina de la lista
    return "".join(cad)#lo que hace es volver a unir la lista en la que se elimino la cadena para unir las partes restantes en este caso sin ningun espacio 

def test_suite():#comprobamos los casos con la funcion
    test(remove_all("an","banana"),"ba")
    test(remove_all("a","arequipa" ),"requip" )
    test(remove_all("i","misti misti" ),"mst mst" )
test_suite()


