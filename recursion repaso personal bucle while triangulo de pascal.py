'''def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(8))
for pedro in [5,7]:
    print(pedro)
a=1
while a<17:
    print(a,"\t",2**a)
    a+=1
for i in range(1,17):
    print(i,"\t",2**i)
#ojo revisar esta funcion para el posible codigo nro 2
def multiplicar_elementos_de_una_lista_con_la_otra(listadeproductos,listadeprecios):
    lista_auxiliar=[]
    for i in range (len(listadeproductos)):
        #for j in range(len(listadeprecios)):
        #if i==j:
        lista_auxiliar.append(listadeproductos[i]*listadeprecios[i])
    return lista_auxiliar
a=[3,4,5,6,7,8,2,7,14,80,40,15]
b=[2,3,5,7,2,7,9,3,2,6,5,4]
print(multiplicar_elementos_de_una_lista_con_la_otra(a,b))'''
#ojo funcion para restar una cantidad a un elemento de la lista
'''def funcion_que_resta_una_a_un_elemento_especifico_de_la_lista(lista,posicion,resta):
    for i in range(len(lista)):
        if i+1==posicion:
            lista[i]-=resta
    return lista    
lista=[3,4,5,9,10]
#lista[1]=1
lista=funcion_que_resta_una_a_un_elemento_especifico_de_la_lista(lista,3,4)
print(lista)
total=0
while True:
    response=input("Introduce el siguiente numero: ")
    if response=="":
        break
    total+=float(response)''
print("El total de la suma es: ",total)
lista=range(19)
for i in lista:
    if i%2==0:
        print(i)
#for i in [12,24,21,27,26,30]:
    #if i%2==1:
        #continue
    #print(i)
count=0
lista=[12,24,21,27,26,30]
while count<len(lista):
    if lista[count]%2==1:
        count+=1
        continue
    #print(lista[count])
    count+=1
lista=["julio","sergio","piero","martin","jose","lucas"]
if "lucas" in lista:
    #print(True)'''
'''import string
def borrar_espacios(message):
    signos=" "
    mensaje1=""
    for i in message:
        if signos in i:
            continue
        mensaje1+=i
    return mensaje1


mensaje="hola a todos"'
print(borrar_espacios(mensaje))'''
'''lista2=[0,1,2,3,4,5,6,7,8,9,10,11,12]
lista2[0:7]=[]
print(lista2)'''
'''lista3=[0,1,2,3,4,5,6,7,8,9,10,11,12]
del lista3[7:]
print(lista3)
for i in range(3):
    print("hello world",i+1)'''
'''def suma_de_elementos_de_una_lista(lista):
    newlist=[]
    for i in range(len(lista)):
        newlist.append(lista[i]+lista[i+1])
    return newlist
def triangulo_Pascal(n):
    lista=[1]
    lista2=[1,1]
    if n==1:
        print(lista)
    elif n==2:
        print(lista,"\n",lista2)
    else:
        lista2.append[1,1]=suma_de_elementos_de_una_lista(triangulo_Pascal(n-1))
        print(lista,"\n",lista2)
triangulo_Pascal(3)'''
my_string = "T E S T"
my_string=my_string.split()
my_string[1:4] = "x","l","m"
print(my_string)