from doctest import _normalize_module
from builtins import print

__author__ = 'Jimenez'

def MostrarDatos(nombre,lugar):
    print("Soy")
    print(nombre)
    print(", vivo en ")
    print(lugar)

#MostrarDatos("Marito Mortadela","San Jose")
#MostrarDatos("Pedrito Morgan","Alajuela")


def ImprimaMayor(valor1,valor2):
    if valor1>valor2:
        print(valor1)
    else:
        print(valor2)

#ImprimaMayor(5,10)


#onfeccionar una función que reciba un entero y luego imprima la tabla de multiplicar
# de dicho valor (por ejemplo si recibe un 3 luego debe mostrar del 3
# hasta el 30 de 3 en 3


def MostrarTabla(num):
    inicio=num
    fin=num*10
    while inicio<=fin:
        print(inicio)
        print('-')
        inicio=inicio+num

#MostrarTabla(3)

#Desarrollar una función que reciba dos enteros y nos muestre todos los
# valores comprendidos entre ellos (el segundo parámetro siempre debe ser mayor.
#  al primero)

def RangoValores(valor1,valor2):
    inicio=valor1
    while inicio<=valor2:
        print(inicio)
        inicio+=1

RangoValores(5,10)