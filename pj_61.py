import itertools
''' dado un numero de cuatro digitos y una lista, se recorre la lista comparando
los ultimos dos digitos de este ultimo con los dos primeros digitos de cada elemento de la 
lista cuando estos sean iguales agrega ese elemento a la lista cumplen,
retorna la lista cumplen con todos los numeros que empiezen con esos dos
digitos'''
def dDinLista(dD, lista):
	cumplen = []
	ns = str(dD)[-2::]
	for i in range(len(lista)):
		if ns == str(lista[i])[0:2]:
			cumplen.append(lista[i])
	return(cumplen)

# inicio de numeros poligonales ----------------------------------------------
'''a continuacion se definen las formas cerradas de los numeros poligonales en
cuestion. Dado un entero n devuelve el n-esimo numero poligonal '''
def P3n(n):
	t = int((n * (n - 1)) / 2)
	return(t)

def P4n(n):
	t = n ** 2
	return(t)

def P5n(n):
	t = int((n * (3 * n - 1)) / 2)
	return(t)

def P6n(n):
	t = n * (2 * n - 1)
	return(t)

def P7n(n):
	t = int((n * (5 * n - 3)) / 2)
	return(t)

def P8n(n):
	t = n * (3 * n - 2)
	return(t)
'''recibe dos parametros, el primero indica de que numero poligonal se quiere
 el n-esimo elemento'''
def nPoligonal(Pn, n): 
	if Pn == 3:
		return(P3n(n))
	elif Pn == 4:
		return(P4n(n))
	elif Pn == 5:
		return(P5n(n))
	if Pn == 6:
		return(P6n(n))
	elif Pn == 7:
		return(P7n(n))
	elif Pn == 8:
		return(P8n(n))
# fin de numeros poligonales -------------------------------------------------

''' generaremos todos los numeros poligonales de orden 3-8 de cuatro cifras
se guardara la lista de los numeros n-poligonales en una lista'''
numeros_poligonales = []
for j in range(3, 9):
	i = 1
	n_poligonal = []
	while(True):
		i += 1
		x = nPoligonal(j, i)

		if x > 9999: # criterio de paro
			break

		if x > 999 and (str(x)[2] != '0'): # 30,181,294,080 - 11,574,182,400 = 18,607,111,680 iteraciones menos :DDDD
			n_poligonal.append(x)

	numeros_poligonales.append(n_poligonal)

''' como el orden del tipo de numero de la cadena de seis no esta propuesto, 
se deben probar todas las permutaciones de las seis listas '''
perm = list(itertools.permutations(numeros_poligonales))
#	indice	numero pentagonal
#	0		triangulares
#	1		cuadrados
#	2		pentagonales
#	3		hexagonal
#	4		heptagonal
#	5		octogonal

# ahora toca lo bueno 

solucion = []
#es un vergeo este algoritmo, alli medio describi que hace chao :D
for l in range(len(perm)):

	permutacion_numeros_poligonales = perm[l]

	for i in range(len(permutacion_numeros_poligonales[0])): # recorre los nummeros triangulares
		N3 = permutacion_numeros_poligonales[0][i]	# toma el i-esimo numero
		cumplen_dD_in_4 = dDinLista(N3, permutacion_numeros_poligonales[1]) # lista de los numeros cuadrados que comienzan con dD de N3

		for j in range(len(cumplen_dD_in_4)): # recorre los numeros cuadrados que cumplen
			N4 = cumplen_dD_in_4[j] # toma el j-esimo numero que cumple
			cumplen_dD_in_5 = dDinLista(N4, permutacion_numeros_poligonales[2]) # lista de los numeros pentagonales que comienzan con dD de N4

			for k in range(len(cumplen_dD_in_5)): # recorre los numeros pentagonales que cumplen
				N5 = cumplen_dD_in_5[k] # toma el j-esimo numero que cumple
				cumplen_dD_in_6 = dDinLista(N5, permutacion_numeros_poligonales[3]) # lista de los numeros hexagonales que comienzan con dD de N5

				for n in range(len(cumplen_dD_in_6)): # recorre los numeros hexagonales que cumplen
					N6 = cumplen_dD_in_6[n] # toma el n-esimo numero que cumple
					cumplen_dD_in_7 = dDinLista(N6, permutacion_numeros_poligonales[4]) # lista de los numeros heptagonal que comienzan con dD de N6

					for m in range(len(cumplen_dD_in_7)):
						N7 = cumplen_dD_in_7[m] # toma el m-esimo numero que cumple
						cumplen_dD_in_8 = dDinLista(N7, permutacion_numeros_poligonales[5])
						if len(cumplen_dD_in_8) != 0:
							if (str(N3)[0:2]) == ( str( cumplen_dD_in_8[0] )[-2::] ):
								sol = [N3, N4, N5, N6, N7, cumplen_dD_in_8[0]]
								solucion.append(sol)

print(solucion)