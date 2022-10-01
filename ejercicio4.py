#Durante la planificación de un proyecto se han acordado una lista de tareas. 
#Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

#¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

#Sugerencia
#Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.


tareas=[[2, "Hacer la cama"], [4, "Recoger la habitacion"], [1, "Subir la persiana"], [3, "Hacer la comida"]]
print(tareas)
tareas_ordenadas = sorted(tareas, key = lambda x:x[0])
#print(tareas_ordenadas)
print(tareas_ordenadas)

#tareas_2 =[]
for i in range (len(tareas_ordenadas)):
    #print(tareas_ordenadas[i,1])