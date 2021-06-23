import random
import math
import operator

Articulos={}
lista_articulos = []
n_soluciones=8
n_articulos = 6
n_cogelones=n_articulos/2
stop=3
evaluacion_ordenada = []
maxOmin = 2
intervalo = 4
n_gen = 3
pesoMax=25
exis=False
tipos=False

def crear_articulos():
	fichero=open('Articulos.txt','r')
	linea=fichero.readline()
	cont=1
	while linea!='':
		x=linea.split(",")
		Articulos[cont]={'Peso':int(x[0]),'Importancia':int(x[1]),'Existencia':int(x[2]),'Tipo':x[3][:-1]}
		linea=fichero.readline()
		cont+=1
	#print(Articulos)

def crear_cromosomas(n_articulos):
    pos=0
    while pos < n_soluciones:
        nuevo_cromosoma = []
        for i in range(0, n_articulos):
        	if exis:
        		n = random.randint(0,Articulos[i+1]['Existencia'])
        	else:
        		n = random.randint(0,1)
        	nuevo_cromosoma.append(n)
        res=restriccion(nuevo_cromosoma)
        lista_articulos.append(nuevo_cromosoma)
        pos+=1
    return lista_articulos

def restriccion(nuevo_cromosoma):
	

def evaluacion(funcion, evaluacion_ordenada, lista_articulos):
    print("######Evaluando individuos######")
    if len(evaluacion_ordenada) > 0:
        evaluacion_ordenada.clear()
    pos = 0
    cromosomas_evaluados = {}
    for lista in lista_articulos:
        peso=0
        importancia=0
        for i in range(0,n_articulos):
        	peso=peso
        evaluacion = math.pow(decimal, 2)
        cromosomas_evaluados[pos] = evaluacion_ordenada
        pos += 1
    evaluacion_ordenada = sorted(
        cromosomas_evaluados.items(), key=operator.itemgetter(1))
    
    return evaluacion_ordenada


def seleccionar(evaluacion_ordenada, lista_articulos, maxOmin):
    print("######Seleccionando individuos######")
    tamaño = len(lista_articulos)
    pos = 0
    if(maxOmin == 1):
        while pos < tamaño / 2:
            print(evaluacion_ordenada[0][0])
            if evaluacion_ordenada[0][0] > (len(lista_articulos) - 1):
                lista_articulos.pop(evaluacion_ordenada[0][0] - pos)
            else:
                lista_articulos.pop(evaluacion_ordenada[0][0])
            evaluacion_ordenada.pop(0)
            pos += 1
            print(lista_articulos)
            print(evaluacion_ordenada)
    elif(maxOmin == 2):
        while pos < tamaño / 2:
            print(evaluacion_ordenada[-1][0])
            if evaluacion_ordenada[-1][0] > (len(lista_articulos) - 1):
                lista_articulos.pop(evaluacion_ordenada[-1][0] - pos)
            else:
                lista_articulos.pop(evaluacion_ordenada[-1][0])
            evaluacion_ordenada.pop(-1)
            pos += 1
            print(lista_articulos)
            print(evaluacion_ordenada)
    return lista_articulos


def lista_a_decimal(lista):
    n_bin = ''.join([str(elem) for elem in lista])
    numero = int(n_bin, 2)
    return numero


def cruzamiento(lista_articulos, intervalo, n_articulos, cont, largo):
    print("#######CRUZAMIENTO#######")
    if (cont+1)<largo:
        nuevo_cromosoma=[]
        pos=0
        while pos<intervalo:
            nuevo_cromosoma.append(lista_articulos[cont][pos])
            pos += 1
        while pos<(len(lista_articulos[0])):
            nuevo_cromosoma.append(lista_articulos[cont+1][pos])
            pos += 1
        print(nuevo_cromosoma)
        lista_articulos.append(nuevo_cromosoma)
        print(lista_articulos)
        nuevo_cromosoma.clear()
        pos=0
        while pos<intervalo:
            nuevo_cromosoma.append(lista_articulos[cont+1][pos])
            pos+=1
        while pos<(len(lista_articulos[0])):
            nuevo_cromosoma.append(lista_articulos[cont][pos])
            pos+=1
        print(nuevo_cromosoma)
        nuevo_cromosoma=mutacion(nuevo_cromosoma)
        lista_articulos.append(nuevo_cromosoma)
        print(lista_articulos)
        cruzamiento(lista_articulos,intervalo,n_articulos,cont+2,largo)
        
def mutacion(cromosoma):
    pos = random.randint(0,7)
    if cromosoma[pos] == 0:
        cromosoma[pos] = 1
    elif cromosoma[pos] == 1:
        cromosoma[pos] = 0
    return cromosoma

if __name__ == '__main__':

    crear_articulos()
    lista_articulos=crear_cromosomas(n_articulos)
    print(lista_articulos)
    #evaluacion_ordenada=evaluacion(0, evaluacion_ordenada,lista_articulos)
    '''for i in range(0,n_gen):
        
        lista_articulos=seleccionar(evaluacion_ordenada,lista_articulos,maxOmin)
        print(lista_articulos)
        cruzamiento(lista_articulos,intervalo,n_articulos,0,len(lista_articulos))'''