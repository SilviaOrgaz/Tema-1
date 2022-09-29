from ctypes.wintypes import HLOCAL
from tkinter import N
#Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

#Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
#Multiplica el numero_usuario por 9 en sí mismo
#Multiplica el numero_magico por el numero_usuario en sí mismo
#Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 12345679
numero_usuario = int(input("Introduzca un numero entre el 1 y el 9:  "))


def mult_numero_usuario(numero_usuario, numero_magico):
    if 0 <= numero_usuario <= 9:
        print("Error no es un numero entre 1 y 9")
        return False
    elif numero_usuario != int(numero_usuario):
        print("Error no es un numero entre 1 y 9")
        return False
    else:
        numero_usuario *= 9
        numero_magico *= numero_usuario 
        print(f"El numero final es : {numero_magico}")
        return numero_magico

numero_final = mult_numero_usuario(numero_usuario, numero_magico)
#print(f"El numero final es : {numero_magico}")



