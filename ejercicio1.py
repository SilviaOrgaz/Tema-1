#Ejercicio 1

#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. 
# Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

#Nombre Apellido ha sacado un Nota de nota.

#Ayuda

#Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"
cadena_ordenada = cadena[::-1]
#print(cadena_ordenada)
#numero_nota = cadena_ordenada[:2]
#nombre = cadena_ordenada[3:]
#print(f"{nombre} ha sacado un {numero_nota} de nota")

#Función que dado una cadena y un separador calcula la posición del separador
def posicion_separador(cadena_ordenada, separador):
    i=0
    while cadena_ordenada[i] != separador:
        i+=1
    return i

posicion = posicion_separador(cadena_ordenada, ",")
print(posicion)
numero = cadena_ordenada[:posicion]
nombre = cadena_ordenada[posicion + 1:]
print(f"{nombre} ha sacado un {numero} de nota")