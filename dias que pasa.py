def number_day(numero):
    semana=["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
    if 0<=numero<len(semana):
        return semana[numero]
def day_number(dia):
    semana=["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
    for i in range(len(semana)):
        if dia == semana[i]:
            return i
def dias_fuera_de_casa(diaquesales,afuera):
    a= day_number(diaquesales)
    resultado=a+afuera
    x=resultado%7
    t=number_day(x)
    return t
l=input("Introduce el día que saldras: ")
m=int(input("Introduce el número de días que estaras fuera de casa: "))
p=dias_fuera_de_casa(l,m)
print("Entonces regresaras el día: ")
print(p)