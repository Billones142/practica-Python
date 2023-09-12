from binarytree import *
import random

lista= range(100)
random.shuffle(lista)

def agregarValorArbol(arbolFuncion,numero):
    if(arbolFuncion == None):
        arbolFuncion= Node(numero)
        return
    if(arbolFuncion.val > numero):
        agregarValorArbol(arbolFuncion.left,numero)
    if(arbolFuncion.val < numero):
        agregarValorArbol(arbolFuncion.left,numero)
        
arbol= Node(1)
agregarValorArbol(arbol, 4)
#agregarValorArbol(arbol, 2)
#agregarValorArbol(arbol, 1)
#agregarValorArbol(arbol, 3)

print(arbol)