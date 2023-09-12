puntuaciones= list()
siNo= list()

def preguntar():
    siNo.append(input("te gusto la presentacion?: "))
    puntuaciones.append(int(input("que puntuacion del 1 al 10 le darias?: ")))

def calcPositivosYNegativos():
    cantSi= 0
    cantNo= 0
    for i in siNo:
        if(i == "si"):
            cantSi+= 1
        else:
            cantNo+= 1
    return cantSi,cantNo

def calcPromedio():
    prom= 0
    for i in puntuaciones: prom+= i
    prom= prom/len(puntuaciones)
    return prom

def informar():
    si, no= calcPositivosYNegativos()
    promedio= calcPromedio()
    print("la cantidad de personas que dijeron si es de ", si)
    print("la cantidad de personas que dijeron no es de ", no)
    print("el promedio es de ", promedio)
    
    
seguirPreguntado= True
while(seguirPreguntado):
    preguntar()
    seguirPreguntado= (input("quiere seguir respondiendo la encuesta?(si , no):") == "no")
    
informar()