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
#5 potencia recursiva
def potencia_recursiva(numero1,numero2):#funcion potencia recursiva
    if numero2==1:#caso base:si el exponente es 1 solo devolvera el numero base por asi decirlo
        return numero1
    else:
        return numero1*potencia_recursiva(numero1,numero2-1)#caso recursivo de no ser asi se entrara en un caso recursivo el cual multiplicara este numero las veces que sea necesaria hasta que restadole una unidad al expoenente este se vuelva 1 para asi terminar con la recursion  
def test_suite():
    test(potencia_recursiva(3,4),81)
    test(potencia_recursiva(7,2),49)
    test(potencia_recursiva(2,5),32)
test_suite()