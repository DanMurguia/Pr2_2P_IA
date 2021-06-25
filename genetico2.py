import random
import math
import operator

Articulos={}
lista_cajas = []
n_soluciones=28
n_articulos = 10
n_cogelones=n_articulos/2
stop=3
evaluacion_ordenada = []
maxOmin = 2
intervalo = 4
intervalo2 = 4
n_gen = 5
pesoMax=25
exis=True
tipos=False
razas = {0:[1,0,0,0,0,0,0,0,1,1,"liquido"],1:[0,1,0,1,0,0,1,0,0,0,"comida"],
         2:[0,0,1,0,1,0,0,0,0,0,"documento"],3:[0,0,0,0,0,1,0,1,0,0,"electronico"],
         4:[1,1,0,1,0,0,1,0,1,1,"licomida"],5:[0,0,1,0,1,1,0,1,0,0,"electromento"],
         6:[0,1,0,1,0,1,1,1,0,0,"elecomida"]}

def crear_articulos():
	fichero=open('Articulos.txt','r')
	linea=fichero.readline()
	cont=1
	while linea!='':
		x=linea.split(",")
		Articulos[cont]={'Peso':int(x[0]),'Importancia':int(x[1]),
                   'Existencia':int(x[2]),'Tipo':x[3][:-1]}
		linea=fichero.readline()
		cont+=1
	print(Articulos)
    
def creacion_razizta(n_articulos,razas,n_soluciones):
    pos=0
    peso=0
    individuos_raza= n_soluciones/7
    individuos = 0
    raza=0
    while pos < n_soluciones:
        nuevo_cromosoma = razas[raza].copy()
        for i in range(0,n_articulos):
            if nuevo_cromosoma[i] == 1:
                nuevo_cromosoma[i] = random.randint(0,Articulos[i+1]['Existencia'])                
        for i in range(0,n_articulos):
            peso=peso+(nuevo_cromosoma[i]*Articulos[i+1]['Peso'])

        if peso <= pesoMax:
            lista_cajas.append(nuevo_cromosoma)
            pos+=1
            individuos += 1            
            if individuos == individuos_raza:
                individuos=0
                raza += 1
        peso = 0
    return lista_cajas
        



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
		print(nuevo_cromosoma)
		for i in range(0,n_articulos):
			peso=peso+(nuevo_cromosoma[i]*Articulos[i+1]['Peso'])
		print(peso)

		if peso <= pesoMax:
				lista_cajas.append(nuevo_cromosoma)
				pos+=1
		peso=0
	return lista_cajas

def evaluacion_razizta(evaluacion_ordenada,lista_cajas,razas):
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
        if importancia == 0:
            evaluacion = 10000
        else:
            evaluacion = peso/importancia
        cromosomas_evaluados[pos] = (evaluacion,lista[n_articulos])
        pos += 1
        
    evaluacion_ordenada = sorted(
        cromosomas_evaluados.items(), key=operator.itemgetter(1))
    return evaluacion_ordenada


def evaluacion(evaluacion_ordenada, lista_cajas):
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
        if importancia == 0:
            evaluacion = 10000
        else:
            evaluacion = peso/importancia
        cromosomas_evaluados[pos] = evaluacion
        pos += 1
    evaluacion_ordenada = sorted(
        cromosomas_evaluados.items(), key=operator.itemgetter(1))
    
    return evaluacion_ordenada


def seleccion_razizta(evaluacion_ordenada,liata_cajas):
    print("######Seleccionando individuos######")
    tamaño = len(lista_cajas)
    pes = 0
    raza = 0
    cont_liquido = 0
    cont_comida = 0
    cont_electronico = 0
    cont_documento = 0
    cont_elecomida = 0
    cont_electromento = 0
    cont_licomida = 0
    suma_total = 0
    pos = -1
    
    
    while suma_total < tamaño / 2:
        
        if evaluacion_ordenada[pos][1][1] == "liquido" and cont_liquido < 2:    
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[pos][0] - pes)
            else:
                lista_cajas.pop(evaluacion_ordenada[pos][0])
            evaluacion_ordenada.pop(pos)
            cont_liquido += 1
            pes += 1
        elif evaluacion_ordenada[pos][1][1] == "comida" and cont_comida < 2:    
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[pos][0] - pes)
            else:
                lista_cajas.pop(evaluacion_ordenada[pos][0])
            evaluacion_ordenada.pop(pos)
            cont_comida += 1
            pes += 1
        elif evaluacion_ordenada[pos][1][1] == "electronico" and cont_electronico < 2:    
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[pos][0] - pes)
            else:
                lista_cajas.pop(evaluacion_ordenada[pos][0])
            evaluacion_ordenada.pop(pos)
            cont_electronico += 1
            pes += 1
        elif evaluacion_ordenada[pos][1][1] == 'documento' and cont_documento < 2:    
            print(evaluacion_ordenada[pos][1][1])
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) -1):
                print(lista_cajas.pop(evaluacion_ordenada[pos][0] - pes))
            else:
                print(lista_cajas.pop(evaluacion_ordenada[pos][0]))
            evaluacion_ordenada.pop(pos)
            cont_documento += 1
            print(cont_documento)
            pes += 1
        elif evaluacion_ordenada[pos][1][1] == "elecomida" and cont_elecomida < 2:    
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[pos][0] - pes)
            else:
                lista_cajas.pop(evaluacion_ordenada[pos][0])
            evaluacion_ordenada.pop(pos)
            cont_elecomida += 1
            pes += 1
        elif  evaluacion_ordenada[pos][1][1] == "electromento" and cont_electromento < 2:    
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[pos][0] - pes)
            else:
                lista_cajas.pop(evaluacion_ordenada[pos][0])
            evaluacion_ordenada.pop(pos)
            cont_electromento += 1
            pes += 1
        elif evaluacion_ordenada[pos][1][1] == "licomida" and cont_licomida < 2:    
            if evaluacion_ordenada[pos][0] > (len(lista_cajas) - 1):
                lista_cajas.pop(evaluacion_ordenada[pos][0] - pes)
            else:
                lista_cajas.pop(evaluacion_ordenada[pos][0])
            evaluacion_ordenada.pop(pos)
            cont_licomida += 1
            pes += 1
        else:
            pos -= 1
            
        suma_total = (cont_liquido + cont_comida+cont_documento+cont_elecomida+
                      cont_electromento+cont_electronico+cont_licomida)

    return lista_cajas


def seleccionar(evaluacion_ordenada, lista_cajas):
    print("######Seleccionando individuos######")
    tamaño = len(lista_cajas)
    pos = 0
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


def cruzamiento(lista_cajas, intervalo, n_articulos, cont, largo,intervalo2):
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
        if exis:
            nuevo_cromosoma=mutacion_chida(nuevo_cromosoma)
        else:
            nuevo_cromosoma=mutacion_simple(nuevo_cromosoma)
        lista_cajas.append(nuevo_cromosoma)
        print(lista_cajas)
        cruzamiento(lista_cajas,intervalo,n_articulos,cont+2,largo, intervalo2)

def deli_razizta(lista_cajas, intervalo, n_articulos, cont, largo,intervalo2):
    print("#######CRUZAMIENTO#######")
    if (cont+1)<largo:
        if lista_cajas[cont][n_articulos] == lista_cajas[cont+1][n_articulos]: 
            print(lista_cajas[cont][n_articulos])
            print(lista_cajas[cont+1][n_articulos])
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
            nuevo_cromosoma2=[]
            pos=0
            while pos<intervalo:
                nuevo_cromosoma2.append(lista_cajas[cont+1][pos])
                pos += 1
            while pos<intervalo2:
                nuevo_cromosoma2.append(lista_cajas[cont][pos])
                pos += 1
            while pos<(len(lista_cajas[0])):
                nuevo_cromosoma2.append(lista_cajas[cont+1][pos])
                pos += 1
            print(nuevo_cromosoma)
            nuevo_cromosoma=mutacion_chida(nuevo_cromosoma)
            lista_cajas.append(nuevo_cromosoma2)
            print(lista_cajas)
            deli_razizta(lista_cajas,intervalo,n_articulos,cont+2,largo,intervalo2)
        
def mutacion_simple(cromosoma):
    print("######Una mutación salvaje ha aparecido######")
    pos = random.randint(0,n_articulos-1)
    if cromosoma[pos] == 0:
        cromosoma[pos] = 1
    elif cromosoma[pos] == 1:
        cromosoma[pos] = 0
    return cromosoma
    
def mutacion_chida(cromosoma):
    pos = random.randint(0,n_articulos-1)
    nueva_cantidad = random.randint(0,Articulos[pos+1]['Existencia'])
    cantidad_original = cromosoma[pos]
    no_disponibles = True
    if nueva_cantidad > cantidad_original:
        print("######Una mutación salvaje ha aparecido######")
        pos2 = random_personalizado([pos],n_articulos-1)
        cromosoma[pos] = nueva_cantidad
        cromosoma[pos2] = random.randint(0,cromosoma[pos2])
        return cromosoma
    elif nueva_cantidad < cantidad_original:
        print("######Una mutación salvaje ha aparecido######")
        pos2 = random_personalizado([pos],n_articulos-1)
        cromosoma[pos] = nueva_cantidad
        cromosoma[pos2]= random.randint(cromosoma[pos2],Articulos[pos2+1]['Existencia'])
        return cromosoma
    else:
        return cromosoma
              
def random_personalizado(exclusiones,rango):
    randInt = random.randint(0,rango)
    return random_personalizado(exclusiones,rango) if randInt in exclusiones else randInt    
 
def resultado(lista_cajas,evaluacion_ordenada):
    print("#######RESULTADO#######")
    evaluacion_ordenada=evaluacion(evaluacion_ordenada,lista_cajas)
    print(evaluacion_ordenada)
    for lista in evaluacion_ordenada:
        print("Cromosoma:"+str(lista_cajas[lista[0]]))
        peso=0
        importancia=0
        for i in range(0,n_articulos):
        	peso=peso+(lista_cajas[lista[0]][i]*Articulos[i+1]['Peso'])
        for i in range(0,n_articulos):
        	importancia=importancia+(lista_cajas[lista[0]][i]*Articulos[i+1]['Importancia'])
        print("Peso:"+str(peso))
        print("Importancia:"+str(importancia))
        print("Evaluacion:"+str(lista[1]))
        print("\n")
    print("#######Mejor resultado#######")
    print("Cromosoma:"+str(lista_cajas[evaluacion_ordenada[0][0]]))
    peso=0
    importancia=0
    for i in range(0,n_articulos):
    	peso=peso+(lista_cajas[evaluacion_ordenada[0][0]][i]*Articulos[i+1]['Peso'])
    for i in range(0,n_articulos):
    	importancia=importancia+(lista_cajas[evaluacion_ordenada[0][0]][i]*Articulos[i+1]['Importancia'])
    print("Peso:"+str(peso))
    print("Importancia:"+str(importancia))
    print("Evaluacion:"+str(evaluacion_ordenada[0][1]))


if __name__ == '__main__':

    for i in range(0,n_gen):
        crear_articulos()
        lista_cajas=creacion_razizta(n_articulos,razas,n_soluciones)
        print(lista_cajas)
        evaluacion_ordenada=evaluacion_razizta(evaluacion_ordenada,lista_cajas,razas)
        print(evaluacion_ordenada)
        lista_cajas=seleccionar(evaluacion_ordenada,lista_cajas)
        print(lista_cajas)
        print(evaluacion_ordenada)
        deli_razizta(lista_cajas,intervalo,n_articulos,0,len(lista_cajas),intervalo2)
    resultado(lista_cajas,evaluacion_ordenada)
        
        