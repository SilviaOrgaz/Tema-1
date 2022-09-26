lista = [4,3,6,1]
lista_ordenada = sorted(lista)
print(lista_ordenada)
lista_pares =[]
lista_impares = []

for i in lista_ordenada:
    if i % 2 == 0:
        lista_par = lista_pares.append(i)
        print(lista_par)
        continue
    elif i % 2!=0:
        lista_impar = lista_impares.append(i)
        print(lista_impar)
        continue
    else:
        break 

