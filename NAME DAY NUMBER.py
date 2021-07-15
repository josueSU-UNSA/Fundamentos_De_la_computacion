print("A continuacion relacionaremos los días desde el domingo al sabado relacionando respectivamente 0 a 6")
def dia_numero (a):
    if a==0:
        return"Domingo"
    elif a==1:
        return"Lunes"
    elif a==2:
        return"Martes"
    elif a==3:
        return"Miercoles"
    elif a==4:
        return"Jueves"
    elif a==5:
        return"Viernes"
    elif a==6:
        return"Sabado"
    return
x= int(input("introduce un número del 0 al 6: "))
a=dia_numero (x)
print(a)    
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

def test_suite():
    test(dia_numero(3),"Miercoles")
    test(dia_numero(6),"Sabado")
    test(dia_numero(42),None)
test_suite()
