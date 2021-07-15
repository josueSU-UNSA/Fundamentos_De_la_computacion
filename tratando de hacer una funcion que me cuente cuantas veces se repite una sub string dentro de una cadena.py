cadena="hola a todos"
cadena=cadena.split()
print(cadena)
punctuation=" ´.;,?[]!"
def borrando_espacios(s):
    s=s.lower()
    s_sans_punct=""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct+=letter
    return s_sans_punct
print(borrando_espacios("Detrás de un salmón\nnada un tiburón,\nlo caza en Alaska\ncansados los dos.\nAsustado grita:\n¡Nooo!, por favor."))
#Aqui esta el problema de buscar una subcadena dentro de una cadena resuelto
def buscando_cadena(oracion,frase):
    contador=0
    oracion=oracion.lower()
    frase=frase.lower()
    for i in oracion.split():
        if frase in i:
            contador+=1
    return contador
'''sentence="hola a todos hola hola hola"
fragmento=input("ingrese el fragmento de coincidencia")'''
print(buscando_cadena("como un pez bajo en agua salada somos buenos momos","mos"))
a=[1,2,3,4,5]
b=[]
for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
     print(i, v)
    

        




