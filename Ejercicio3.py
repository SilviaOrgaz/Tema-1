#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas.
# pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

#Así recorreria la lista por indices pero no estaría bien programado porque las listas tienen distinta longitud.
#def lista_repetir(lista_1, lista_2):
    #lista_3 = []
    #for i in range(len(lista_2)):
        #if lista_1[i] == lista_2[i]:
            #lista_3.append(lista_1[i])
    #return lista_3

#lista_3 = lista_repetir(lista_1, lista_2)
#(lista_3)

#Función que dada dos lista devuelve una lista con elementos comunes. Va recorriendo los elementos en vez de las posiciones
def lista_repetir_2(lista_1, lista_2):
    lista_3=[]
    for i in lista_2:
        if i in lista_1 and i not in lista_3:
            lista_3.append(i)
    return lista_3

lista = lista_repetir_2(lista_1, lista_2)
print(lista)

