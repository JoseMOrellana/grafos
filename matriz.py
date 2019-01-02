def buscar_grados_impares(lista):
	"""Retorna un booleano que indica si hay o no grados impares en el grafo e 
	indica cuantos grados impares hay en caso que si halla"""
	noGradoImpar,numGradosImpares = True,0
	for grado in lista:
		if grado % 2 != 0:
			noGradoImpar = False
			numGradosImpares += 1
	return noGradoImpar,numGradosImpares

def calcular_grados(matriz):
	"""Crea una lista con los grados de cada nodo"""
	lista = []
	for i in range(len(matriz)):
		suma = 0
		suma = grado_nodo(matriz,i)
		lista.append(suma)
	return lista

def euler(matriz,grados):
	"""Calcula si el grafo contiene circuito o camino euleriano"""
	sinGradoImpar, numGradosImpares = buscar_grados_impares(grados)
	if (sinGradoImpar):
		print("Existe camino y circuito euleriano")
		return True
	elif(numGradosImpares == 2):
		print("No existe circuito euleriano, sin embargo si existe camino")
	else: 
		print("No existe ni camino ni ciclo euleriano")
	return False
	
	print(grados)

def hamilton(grados):
	"""Calcula si el grafo contiene circuito o camino hamiltoniano"""
	maximo = 0
	condicion = len(grados) - 1
	for i in range(len(grados) - 1):
		for j in range(i + 1,len(grados)):
			suma = grados[i] + grados[j]
			maximo = max(maximo,suma)
	if maximo > condicion: return True
	return False


	


def grado_nodo(matriz,pos):
	"""Retorna el grado de un nodo dada su posicion y la matriz adyacencia"""
	suma = 0
	for i in range(len(matriz[pos])):
		suma +=  matriz[pos][i]
	return suma


def grafo_conexo(matriz):
	"""Dada una matriz de adyacencia determina si el grafo es conexo"""
	conectados = dict()
	no_conectados = dict()
	for i in range(len(matriz)):
		conectados[i] = []
		no_conectados[i] = []
		for j in range(len(matriz)):
			if i == j:
				continue
			conectados[i].append(j) if matriz[i][j] > 0 else no_conectados[i].append(j)
	
	lista_aux = []
	conexo = True
	for nodo in conectados:
		while conectados[nodo] != lista_aux or len(conectados[nodo]) < len(matriz) - 1:
			lista_aux = conectados[nodo] 
			for n in lista_aux:
				ext = conectados[n]
				for e in ext: 
					if e not in conectados[nodo] and e != nodo:
						conectados[nodo].append(e)
		result =  all(elem in conectados[nodo]  for elem in no_conectados[nodo])
		conexo = conexo and result
	return conexo


def run(matriz):
	grados = calcular_grados(matriz)
	conexo = grafo_conexo(matriz)
	g_euler = g_hamilton = False
	if conexo:
		g_euler = euler(matriz,grados)
		g_hamilton = hamilton(grados)
	print("Euler: {}".format(g_euler))
	print("Hamilton: {}".format(g_hamilton))

			#A 	B 	C 	D 
matriz = [
		 	[0,	1,	1,	0], #A
		 	[1,	0,	0,	1], #B
		 	[1,	0,	0,	1], #C
		 	[0,	1,	1,	0] #D
		 ]

run(matriz)