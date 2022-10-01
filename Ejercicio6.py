#Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares y la segunda con los números impares.
#Por ejemplo:
#pares, impares = separar([6,5,2,1,7])
#prnt(pares)
#print(impares)
#[2, 6]
#[1, 5, 7]
#Sugerencia
#Para ordenar una lista automáticamente puedes utilizar el método .sort().

lista = [6,5,2,1,7]
#lista.sort()
lista_ordenada = sorted(lista)
#lista_pares = []
#lista_impares = []

def separar_lista(lista):
    lista_pares_funcion = []
    lista_impares_funcion =[]
    for i in lista:
        if i % 2 == 0:
            lista_pares_funcion.append(i)
        else:
            lista_impares_funcion.append(i)
    return lista_impares_funcion, lista_impares_funcion

lista_pares, lista_impares=separar_lista(lista_ordenada)
print(lista_pares)
print(lista_impares)




