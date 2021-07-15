def vuelves (f,e):
    fv=f+e+1#es mas 1 por que contamos al dia ultimo de estadia
    if fv == 0 or fv==7:
        return"domingo"
    elif fv==1 or fv==8:
        return "lunes"
    elif fv==2 or fv==9:
        return "Martes"
    elif fv==3 or fv==10:
        return"miercoles"
    elif fv==4 or fv==11:
        return"jueves"
    elif fv==5 or fv==12:
        return"viernes"
    elif fv==6 or fv==13:
        return"sabado"
    else :
        print("ingrese los datos correctos porfavor")
        return
a=int(input("introduce un número del 0 al 6 teniendo en consideradción que:\nestos representan el orden de los días del domingo al sabado respectivamente: "))
b=int(input("introduce los días de estadia que estuvistes"))
c=vuelves(a,b)
print(c)