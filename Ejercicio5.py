#Crea un script llamado descomposicion.py que realice las siguientes tareas:
#Debe tomar 1 argumento que será un número entero positivo.
#En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
#El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:
#python descomposicion.py 3647
#El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
#0007
#0040
#0600
#3000
#Pista
#Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. 
#Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa


#Esto es una función que deetcta si es un numero positivo, negativo  o no es un numero.
def detectar_numero_positivo(numero):
    try:
        numero = int(numero)
    except:
        print("Debes introducir un número")
        return -1
    if numero >= 0:
        print("Genial")
    else:
        print("Este número no es positivo")  
    return numero

detectar_numero=-1
while detectar_numero < 0:
    numero = input("Introduce un número positivo: ")
    detectar_numero = detectar_numero_positivo(numero)

numero_cadena = [int(x) for x in str(detectar_numero)]
print(numero_cadena)

#numeros = numero_cadena[-1]
#print(numeros)
longitud_numero_cadena = len(numero_cadena)

i=0
for i in range(longitud_numero_cadena):
    numeros = numero_cadena[-1-i]*10**i
    i+=1
    #numeros.append(i)
    print(numeros)








