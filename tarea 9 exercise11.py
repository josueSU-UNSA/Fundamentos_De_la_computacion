import sys
def compare (a,b):
    if a>b :
        return 1
    elif a==b:
        return 0
    return -1
j=int(input("Introduce el primero número: "))
n=int(input("Introduce el siguiente número: "))
b=compare(j,n)
print(b)  
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
    test(compare (5,4),1)
    test(compare (7,7),0)
    test(compare (2,3),-1)
    test(compare (42,1),1)
    
test_suite()

