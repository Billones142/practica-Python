import csv
import os
from pathlib import Path

archivoDeUsuarios= os.path.join(os.path.abspath(os.path.dirname(__file__)), "usuarios.csv")
archivoDePedidos= os.path.join(os.path.abspath(os.path.dirname(__file__)), "pedidos.csv")
archivoEmpleados= os.path.join(os.path.abspath(os.path.dirname(__file__)), "empleados.csv")
archivoEntradaYSalida= os.path.join(os.path.abspath(os.path.dirname(__file__)), "entradaYSalida.csv")
archivoPagos= os.path.join(os.path.abspath(os.path.dirname(__file__)), "pagos.csv")
archivoStock= os.path.join(os.path.abspath(os.path.dirname(__file__)), "stock.csv")

def login(usuario, contraseña):
    with open(archivoDeUsuarios, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for linea in spamreader:
            if(linea[0] == usuario):
                if(linea[1] == contraseña):
                    return True
    return False

def infoPedidos():
    cantDeLineas= 0
    with open(archivoDePedidos) as csvfile:
        Lineas= csv.reader(csvfile, delimiter=",", quotechar="|")
        for linea in Lineas:
            cantDeLineas+=1
            
    return cantDeLineas

def cantEmpleados():
    cantDeLineas= 0
    with open(archivoEmpleados) as csvfile:
        Lineas= csv.reader(csvfile, delimiter=",", quotechar="|")
        for linea in Lineas:
            cantDeLineas+=1
    
    return cantDeLineas

def nombreEmpleado(numero):
    lista=[]
    with open(archivoEmpleados, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for linea in spamreader:
            lista.append(linea[0])
    return lista[numero]

def cantHorarioEmpleado(numero):
    lista= []
    with open(archivoEntradaYSalida, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for linea in spamreader:
            lista.append(linea[0])
    return len(lista)

def horariosEmpleado(numero):
    lista= []
    with open(archivoEntradaYSalida, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i= 0
        for linea in spamreader:
            if i==numero:
                for x in range(len(linea)):
                    lista.append(linea[x])
            i+= 1
    return lista

def pedidoN(numero):
    lista= []
    with open(archivoDePedidos, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i= 0
        for linea in spamreader:
            if i==numero:
                for x in range(len(linea)):
                    lista.append(linea[x])
            i+= 1
    return lista


def cantEnvios():
    lista= []
    i= 0
    with open(archivoDePedidos, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for linea in spamreader:
            i+= 1
    return i

def pagoN(numero):
    lista= []
    with open(archivoPagos, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i= 0
        for linea in spamreader:
            if i==numero:
                for x in range(len(linea)):
                    lista.append(linea[x])
            i+= 1
    return lista


def cantPagos():
    lista= []
    i= 0
    with open(archivoStock, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for linea in spamreader:
            i+= 1
    return i

def stockN(numero):
    datos= []
    with open(archivoStock, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i= 0
        for linea in spamreader:
                if i==numero:
                    datos= linea
                
                i+= 1
    return datos

def cantTiposStock():
    lista= []
    i= 0
    with open(archivoStock, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for linea in spamreader:
            i+= 1
    return i