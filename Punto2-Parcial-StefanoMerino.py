from binarytree import *
import random

preorder= "GEAIBMCLDFKJH"
inorder= "IABEGLDCFMKHJ"

preorder2= list()
for i in preorder:
    preorder2.append(i)

arbol= build(preorder2)

def devolverLista():
    lista= arbol.preorder
    lista2= list()
    for i in lista:
        lista2.append(i.val)
    return lista2

preorder3= list()
for i in preorder2:
    preorder3.append(i)

while(preorder2 != devolverLista()):  #prueba hasta que algun dia lo encuetre...
    random.shuffle(preorder3)
    arbol= build(preorder3)
    print(preorder2)
    print(devolverLista())
    print()


print(arbol)
print(arbol.preorder)