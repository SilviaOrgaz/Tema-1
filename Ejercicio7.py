#Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

#Error: Imposible añadir elementos duplicados => [elemento].
#Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

#Sugerencia

#Puedes utilizar la sintaxis "elemento in lista"

#elementos = [1, 5, -2]


#from multiprocessing.dummy import Value



def agregar_una_vez(lista, elemento):
    if elemento in lista:
        #print(f"Error: Imposible añadir elementos duplicados =>{elemento}")
        raise ValueError
    else:
        lista.append(elemento)
    return lista

lista= [1, 5, -2]
try:
    elemento = -2
    generar_lista = agregar_una_vez(lista, -2)
except ValueError:
    print(f"Error: Imposible añadir elementos duplicados => {elemento}")
try:
    elemento=10
    generar_lista = agregar_una_vez(lista, 10)
except ValueError:
    print(f"Error: Imposible añadir elementos duplicados => {elemento}")
try:
    elemento = "Hola"
    generar_lista = agregar_una_vez(lista, "Hola")
except ValueError:
    print(f"Error: Imposible añadir elementos duplicados => {elemento}")

print(f"La lista final es: {generar_lista}")







