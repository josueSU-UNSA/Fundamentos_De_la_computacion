#break bucle while

#ejercicio


def find_index (str, c):
    for i in range(len(str)):
        if  c == str[i] :
            return(i)
cadena = "cienciae"
print(find_index(cadena, "e"))
#con while
def find_index_w(str,c):
    i=0
    while i <len(str):
        if c==str[i]:
            return i
        i+=1