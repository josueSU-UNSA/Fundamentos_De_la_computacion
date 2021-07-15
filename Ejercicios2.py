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
#2 division exacta y residuo  
def division_exacta_residuo(numero1, numero2):
    a=numero1//numero2#el operador // me retorna una division exacta
    b=numero1%numero2#el operador % me retorna el residuo de una division
    #return "La division exacta de {} y {} es {}\nEl residuo es {}".format(numero1,numero2,a,b)#se aplico el metodo format para devolver el texto con la finalidad de incorporarlo directamente a la funcion
    return (a,b)#al utilizar la funcion test es preferible usar mejor una tupla

def test_suite():
    test(division_exacta_residuo(8,5),(1,3) )
    test(division_exacta_residuo(10,5),(2,0) )
    test(division_exacta_residuo(9,4),(2,1) )
test_suite()