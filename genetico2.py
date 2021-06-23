import random
import math
import operator

Articulos={}
lista_cajas = []
n_soluciones=8
n_articulos = 6
n_cogelones=n_articulos/2
stop=3
evaluacion_ordenada = []
maxOmin = 2
intervalo = 2
intervalo2 = 4
n_gen = 3
pesoMax=25
exis=False
tipos=False
razas=[]

def crear_articulos():
	fichero=open('Articulos.txt','r')
	linea=fichero.readline()
	cont=1
	while linea!='':
		x=linea.split(",")
		Articulos[cont]={'Peso':int(x[0]),'Importancia':int(x[1]),'Existencia':int(x[2]),'Tipo':x[3][:-1]}
		linea=fichero.readline()
		cont+=1
	print(Articulos)

def crear_cromosomas(n_articulos):
	pos=0
	peso=0
	while pos < n_soluciones:
		nuevo_cromosoma = []
		for i in range(0, n_articulos):
			if exis:
				n = random.randint(0,Articulos[i+1]['Existencia'])
			else:
				n = random.randint(0,1)
			nuevo_cromosoma.append(n)
		for i in range(0,n_articulos):
			peso=peso+(nuevo_cromosoma[i]*Articulos[i+1]['Peso'])
		print(nuevo_cromosoma)
		print(peso)
		if peso <= pesoMax:
			if tipos:
				res=restriccion(nuevo_cromosoma)
				if res:
					lista_cajas.append(nuevo_cromosoma)
					pos+=1
			else:
				lista_cajas.append(nuevo_cromosoma)
				pos+=1
		peso=0
	return lista_cajas

def restriccion(nuevo_cromosoma):
    raza=razear(nuevo_cromosoma)
    print(raza)
    if raza=="L" or raza=="LC" or raza=="C" or raza=="E" or raza=="D" or raza=="CE" or raza=="ED":
        res=True
    else:
        rest=False
    return rest

def razear(nuevo_cromosoma):
	L=0
	C=0
	E=0
	D=0
	raza=""
	for i in range(0,n_articulos):
		if (nuevo_cromosoma[i]>1):
			print(Articulos[i+1]['Tipo'])
			if (Articulos[i+1]['Tipo']=='Liquid'):
				L+=1
			if (Articulos[i+1]['Tipo']=='Food'):
				C+=1
			if (Articulos[i+1]['Tipo']=='Document'):
				D+=1
			if (Articulos[i+1]['Tipo']=='Electronic'):
				E+=1
	if L>=1:
		raza="L"
		if C>=1:
			raza="LC"
			if E>=1:
				raza="LCE"
				if D>=1:
					raza="LCED"
			else:
				if D>=1:
					raza="LCD"
		else:
			if E>=1:
				raza="LE"
				if D>=1:
					raza="LED"
			else:
				if D>=1:
					raza="LD"
	if C>=1:
		raza="C"
		if E>=1:
			raza="CE"
			if D>=1:
				raza="CED"
		else:
			if D>=1:
				raza="CD"
	if E>=1:
		raza="E"
		if D>=1:
			raza="ED"
	if D>=1:
		raza="D"

	return raza


def evaluacion(funcion, evaluacion_ordenada, lista_cajas):
    print("######Evaluando individuos######")
    if len(evaluacion_ordenada) > 0:
        evaluacion_ordenada.clear()
    pos = 0
    cromosomas_evaluados = {}
    for lista in lista_cajas:
        peso=0
        importancia=0
        for i in range(0,n_articulos):
        	peso=peso+(lista[i]*Articulos[i+1]['Peso'])
        for i in range(0,n_articulos):
        	importancia=importancia+(lista[i]*Articulos[i+1]['Importancia'])
        evaluacion = peso/importancia
        cromosomas_evaluados[pos] = evaluacion
        pos += 1
    evaluacion_ordenada = sorted(
        cromosomas_evaluados.items(), key=operator.itemgetter(1))
    
    return evaluacion_ordenada


def seleccionar(evaluacion_ordenada, lista_cajas, maxOmin):
    print("######Seleccionando individuos######")
    tamaño = len(lista_cajas)
    pos = 0
    if tipos:
        while pos < tamaño / 2:
            print(evaluacion_ordenada[0][0])
            if evaluacion_ordenada[0][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[0][0] - pos)
            else:
                lista_cajas.pop(evaluacion_ordenada[0][0])
            evaluacion_ordenada.pop(0)
            pos += 1
            print(lista_cajas)
            print(evaluacion_ordenada)
    else:
        while pos < tamaño / 2:
            print(evaluacion_ordenada[-1][0])
            if evaluacion_ordenada[-1][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[-1][0] - pos)
            else:
                lista_cajas.pop(evaluacion_ordenada[-1][0])
            evaluacion_ordenada.pop(-1)
            pos += 1
            print(lista_cajas)
            print(evaluacion_ordenada)
    return lista_cajas


def cruzamiento(lista_cajas, intervalo, n_articulos, cont, largo):
    print("#######CRUZAMIENTO#######")
    if (cont+1)<largo:
        nuevo_cromosoma=[]
        pos=0
        while pos<intervalo:
            nuevo_cromosoma.append(lista_cajas[cont][pos])
            pos += 1
        while pos<intervalo2:
            nuevo_cromosoma.append(lista_cajas[cont+1][pos])
            pos += 1
        while pos<(len(lista_cajas[0])):
            nuevo_cromosoma.append(lista_cajas[cont][pos])
            pos += 1
        print(nuevo_cromosoma)
        lista_cajas.append(nuevo_cromosoma)
        print(lista_cajas)
        nuevo_cromosoma.clear()
        pos=0
        while pos<intervalo:
            nuevo_cromosoma.append(lista_cajas[cont+1][pos])
            pos += 1
        while pos<intervalo2:
            nuevo_cromosoma.append(lista_cajas[cont][pos])
            pos += 1
        while pos<(len(lista_cajas[0])):
            nuevo_cromosoma.append(lista_cajas[cont+1][pos])
            pos += 1
        print(nuevo_cromosoma)
        #nuevo_cromosoma=mutacion(nuevo_cromosoma)
        lista_cajas.append(nuevo_cromosoma)
        print(lista_cajas)
        cruzamiento(lista_cajas,intervalo,n_articulos,cont+2,largo)
        
def mutacion(cromosoma):
    pos = random.randint(0,7)
    if cromosoma[pos] == 0:
        cromosoma[pos] = 1
    elif cromosoma[pos] == 1:
        cromosoma[pos] = 0
    return cromosoma

if __name__ == '__main__':

    crear_articulos()
    lista_cajas=crear_cromosomas(n_articulos)
    print(lista_cajas)
    evaluacion_ordenada=evaluacion(0, evaluacion_ordenada,lista_cajas)
    print(evaluacion_ordenada)
    lista_cajas=seleccionar(evaluacion_ordenada,lista_cajas,maxOmin)
    cruzamiento(lista_cajas,intervalo,n_articulos,0,len(lista_cajas))
    '''for i in range(0,n_gen):
        
        
        print(lista_cajas)
        cruzamiento(lista_cajas,intervalo,n_articulos,0,len(lista_cajas))'''