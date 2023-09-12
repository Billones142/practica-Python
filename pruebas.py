from binarytree import *

arbol= None

def cargarValor(a,valor):
    global arbol
    if(arbol is None):
        arbol= Node(valor)
    else:       
        if(a.val < valor):
            if(a.left is None):
                a.left= Node(valor)
            else:
                cargarValor(a.left,valor)
    
        if(a.val > valor):
            if(a.right is None):
                a.right= Node(valor)
            else:
                cargarValor(a.right,valor)

cargarValor(arbol,1)
cargarValor(arbol,-2)
cargarValor(arbol,8)

print(arbol)