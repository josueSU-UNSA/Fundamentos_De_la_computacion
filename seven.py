import sys

def test(actual, expected):
    linenum = sys._getframe(1).f_lineno  
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg) 
    
def to_secs  (horas, minutos, segundos):
    return(horas * 3600 + minutos* 60 + segundos)

#esto es lo que tu hiciste
# def test_suite(3600):
    #test(to_secs(1,0,0)
def test_suite():
    test(to_secs(1,0,0),3600)#en esta parte se pone la funcion , lo que se espera 

test_suite()        # Here is the call to run the tests