"""
El centro de atención telefónica del banco Patagones maneja una cola para las
llamadas entrantes, 
en la cual cada llamada tiene una prioridad entre dos posibles: 1 ó 2,
siendo 1 la prioridad más alta (clientes del banco) y es la que se debe atender primero, 
y 2 la prioridad más baja (público en general). 
En hora pico, el número promedio de llamadas es de 10 (diez). Se pide:
    a. Implemente una cola con prioridad, tal que cuando ingresa una llamada esta debe
       ubicarse en la cola de tal modo que todos los que estén delante de él tengan mayor o
       igual prioridad.
    b. Para cada llamada indique el orden de ingreso y el orden de atención.
    c. Calcule el porcentaje de llamadas de cada tipo. 
"""
import random

colaDeLlamada= [0 for i in range(10)]  # el numero mas bajo tiene mas prioridad
ordenDeLLegada= [random.randint(1,2) for i in range(10)]
llamadasConPrioridad= 0
llamadasSinPrioridad= 0

def agregarConPrioridad(ticket,num):
    if(num != 10):
        num+= 1
        if(colaDeLlamada[num-1] != 0):
            agregarConPrioridad(ticket,num)
        else:
            colaDeLlamada[num-1]= ticket

def agregarSinPrioridad(ticket,num):
    if(num != 0):
        if(colaDeLlamada[num] != 0):
            agregarSinPrioridad(ticket,num-1)
        else:
            colaDeLlamada[num]= ticket

for i in range(len(ordenDeLLegada)):
    if(ordenDeLLegada[i] == 1):
        agregarConPrioridad(i+1,0)
        llamadasConPrioridad+= 1
    else:
        agregarSinPrioridad(i+1,9)
        llamadasSinPrioridad+= 1

print("cola de llegada:")
print(ordenDeLLegada)

print("la cola quedo organizada de la siguiete manera(menor numero tiene mas prioridad)")
for i in range(10):
    print(i,": con ticket: ", colaDeLlamada[i])
print("las llamadas con prioridad fueron del ", llamadasConPrioridad*10,"%")
print("las llamadas sin prioridad fueron del ", llamadasSinPrioridad*10,"%")