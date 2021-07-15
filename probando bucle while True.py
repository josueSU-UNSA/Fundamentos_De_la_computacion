def borrar_todo(lista):
    lista[:]=[]
lista1=[1,2,3,4,5,6]
print(borrar_todo(lista1))    
def manipular_producto_venta(lista,orden_del_producto,cambiar_producto,cambiar_precio):
    lista[orden_del_producto-1]=(cambiar_producto,cambiar_precio)
def funcion_mostrar_productos_de_venta(lista):
    for i in range(len(lista)):
        print("{:<5}\t{:<10}\t{:>5}".format(i+1,lista[i][0],lista[i][1]))
def calcular_total(lista):
    count=0
    for i in range(len(lista)):
        count+=lista[i][2]
    return count
def buscar_producto(lista,orden):
    return lista[orden-1][0]
def buscar_valor_producto(listavent,orden):
    return listavent[orden-1][1]
def funcion_mostrar_elementos_de_compra(listacompra):
    for i in range(len(listacompra)):
        print("{:<5}\t{:<10}\t{:>5}\t{:>12}".format(i+1,listacompra[i][0],listacompra[i][1],listacompra[i][2]))
lista_de_compra=[]
lista_de_venta=[]
while True:
    print("---------------------------------------------------------------------------------------------------------------------")
    print("1.Administrador de productos")
    print("2.Comprar productos")
    print("3.Salir")
    print("---------------------------------------------------------------------------------------------------------------------")
    a=int(input("-Ingrese su perfil: "))
    print("---------------------------------------------------------------------------------------------------------------------")
    if a==1:
        print("1.Agregar producto a la lista de venta")
        print("2.Manipular producto")
        print("3.ver lista")
        print("4.Borrar toda la lista ")
        print("5.Salir de la opcion administrador")
        print("---------------------------------------------------------------------------------------------------------------------")
        b=int(input("-Ingrese opcion: "))
        print("---------------------------------------------------------------------------------------------------------------------")
        while b<=4:
            if b==1:
                c=input("1-Ingrese el nombre del producto: ")
                d=float(input("2-Ingrese el costo del producto: "))
                print("---------------------------------------------------------------------------------------------------------------------")
                z=(c,d)
                lista_de_venta.append(z)
                print("---------------------------------------------------------------------------------------------------------------------")
                print("1.Seguir añadiendo producto\n2.Ir a la opcion manipular productos\n3.Ver la lista de productos a vender\n4.Borrar toda la lista\n5.Salir de la opcion administrador")
                print("---------------------------------------------------------------------------------------------------------------------")
                b=int(input("-Ingrese opcion: "))
                print("---------------------------------------------------------------------------------------------------------------------")
            if b==2:
                if len(lista_de_venta)!=0:
                    a1="LISTA DE VENTA"
                    a2="Orden"
                    a3="Producto"
                    a4="Precio por unidad"
                    print("{:^30}\n{:<5}\t{:<10}\t{:>5}".format(a1,a2,a3,a4))
                    funcion_mostrar_productos_de_venta(lista_de_venta)
                    y=int(input("1-Ingrese el orden del producto: "))
                    x=input("2-Ingrese el nombre del producto el cual agregaras: ")
                    w=float(input("3-Ingresa el precio del producto: "))
                    manipular_producto_venta(lista_de_venta,y,x,w)
                    print("---------------------------------------------------------------------------------------------------------------------")
                    print("1.Añadir producto a la lista de venta\n2.Seguir manipulando productos\n3.Ver la lista de productos a vender\n4.Borrar toda la lista\n5.Salir de la opcion administrador")
                    print("---------------------------------------------------------------------------------------------------------------------")
                    b=int(input("-Ingrese opcion: "))
                else:
                    print("Aun no agrego ningún producto ,empiece agregando un producto")
                    print("---------------------------------------------------------------------------------------------------------------------")
                    print("1.Añadir producto a la lista de venta\n2.Seguir manipulando productos\n3.Ver la lista de productos a vender\n4.Borrar toda la lista\n5.Salir de la opcion administrador")
                    print("---------------------------------------------------------------------------------------------------------------------")
                    b=int(input("Ingrese opcion: "))
            if b==3:
                print("---------------------------------------------------------------------------------------------------------------------")
                v="LISTA DE VENTA"
                ab2="Orden"
                ab3="Producto"
                ab4="Precio por unidad"
                print("{:^30}\n{:<5}\t{:<10}\t{:>5}".format(v,ab2,ab3,ab4))
                funcion_mostrar_productos_de_venta(lista_de_venta)
                print("---------------------------------------------------------------------------------------------------------------------")
                print("¿Ahora que desea hacer?:")
                print("1.Añadir producto a la lista de venta\n2.Manipular producto\n3.Ver la lista de productos a vender\n4.Borrar toda la lista\n5.Salir de la opcion administrador")
                b=int(input("Ingrese opcion: "))
            if b==4:
                borrar_todo(lista_de_venta)
                print("---------------------------------------------------------------------------------------------------------------------")
                print("1.Añadir producto a la lista de venta\n2.Manipular producto\n3.Ver la lista de productos a vender\n4.Borrar toda la lista\n5.Salir de la opcion administrador")
                print("---------------------------------------------------------------------------------------------------------------------")
                b=int(input("Ingrese opcion: "))
    elif a==2 and len(lista_de_venta)!=0:
        print("---------------------------------------------------------------------------------------------------------------------") 
        print("1.Agregar cosas al carro de compra\n2. Ver la lista de compras actual\n3.Ver el total a pagar\n4.Salir del modo comprador")
        print("---------------------------------------------------------------------------------------------------------------------")
        c=int(input("-Ingrese opcion: "))
        while c<4 :
            if c==1:
                
                print("---------------------------------------------------------------------------------------------------------------------")
                funcion_mostrar_productos_de_venta(lista_de_venta)
                j=int(input("1-Ingrese el orden en el cual se encuentra el producto que quiere comprar: "))
                o=float(input("2-Ingrese la cantidad que llevara del producto: "))
                print("---------------------------------------------------------------------------------------------------------------------")
                #f=(buscar_producto(lista_de_venta,j),o)
                p=buscar_producto(lista_de_venta,j)
                s=(buscar_valor_producto(lista_de_venta,j)*o)
                u=(p,o,s)
                lista_de_compra.append(u)
                print("1.Seguir agregando cosas al carro\n2.Ver la lista de compras actual\n3.Ver el total a pagar\n4.Salir del modo comprador")
                print("---------------------------------------------------------------------------------------------------------------------")
                c=int(input("-Ingrese opcion: "))
            if c==2:
                print("---------------------------------------------------------------------------------------------------------------------")
                f="LISTA DE COMPRA"
                f1="Orden"
                f2="Producto"
                f3="Cantidad"
                f4="Total"
                print("{:^30}\n{:<5}\t{:<10}\t{:>5}\t{:<5}".format(f,f1,f2,f3,f4))
                funcion_mostrar_elementos_de_compra(lista_de_compra)
                print("---------------------------------------------------------------------------------------------------------------------")
                print("1.Agregar cosas al carro\n2.Ver la lista de compras actual\n3.Ver el total a pagar\n4.Salir del modo comprador")
                c=int(input("Ingrese opcion: "))
            if c==3:
                print("---------------------------------------------------------------------------------------------------------------------")
                print("El total a pagar seria: {}.".format(calcular_total(lista_de_compra)))
                print("---------------------------------------------------------------------------------------------------------------------")
                print("1.Agregar cosas al carro\n2.Ver la lista de compras actual\n3.Ver el total a pagar\n4.Salir del modo comprador")
                c=int(input("-Ingrese opcion: "))
    elif a==2 and len(lista_de_venta)==0:
        print("Aun no puedes comprar ningun producto por que el vendedor aun no agrego mercaderia")
    elif a==3:
        print("Espero el programa haya sido de su agrado")
        break
    else:
        print("Seleccion no válida\nPorfavor use una de las opciones permitidas gracias:")
        
        