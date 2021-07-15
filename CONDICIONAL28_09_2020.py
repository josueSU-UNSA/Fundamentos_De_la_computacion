a=7
b=7
c=7
if a<=b and b<=c:
    print(str(c)+" es el maximo y ",a," el minimo")
elif a<=c and c<=b:
    print(str(b)+ " es el maximo y " ,a , " el minimo")
elif b<=a and a<=c:
    print(str(c) + " es el maximo y ", b , " el minimo")
elif b<=c and c<=a:
    print(str(a)+ " es el maximo y ",b, " el minimo")
elif c<=a and a<=b:
    print(str(b)+" es el maximo y ",c," el minimo")
elif c<=b and b<=a:
    print(str(a)+" es el maximo y " ,c , " el minimo")

a=int(input("introduzca un numero"))
b=int(input("introduzca un numero"))
if a==b :
    print("a es igual a b")
elif a<b:
    print("a es menor que b")
else:
    print("a es mayor que b")
a=int(input("introduzca un numero"))
if a>=0  and a<=10:
    print("si esta en el intervalo de 0 a 10")
else:
    print("no se encuentra en este intervalo")