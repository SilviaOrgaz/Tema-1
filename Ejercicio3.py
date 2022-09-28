#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas.
# pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

#def lista_repetir(lista_1, lista_2):
    #lista_3 = []
    #i=0
    #while lista_1[i] == lista_2[i]:
        #lista_3.append(i)
        #i+=1
    #return lista_3

#lista_3 = lista_repetir(lista_1, lista_2)
#print(lista_3)

def lista_repetir_2(lista_1, lista_2):
    lista_3=[]
    for i in lista_2:
        if i in lista_1 and i not in lista_3:
            lista_3.append(i)
    return lista_3

lista_3 = lista_repetir_2(lista_1, lista_2)
print(lista_3)

