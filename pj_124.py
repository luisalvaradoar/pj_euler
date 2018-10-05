import math

# criba de eratostenes para probar si un numero 'n' es primo. Prueba a n mod k para k < sqrt(n)
def eratostenes( n ):
	if n == 1:
		return( 0 )
	else:
		for i in range( 2 , int( math.floor( math.sqrt( n ) ) ) + 1 ):
			if n % i == 0:
				return( 0 )
		return( n )

'''funcion rad, si n es primo devuelve n. Sino, calcula los primos p < n/2 
tal que p|n, los pone en una lista y al final recorre la lista multiplicando
sus elementos'''
def rad(n):
	if eratostenes(n) != 0:
		return(n)
	lista_primos = []
	P = 1
	for i in range(round(n/2)+1):
		if eratostenes(i) != 0:
			if n % eratostenes(i) == 0:
				lista_primos.append(i)
	for j in range(len(lista_primos)):
		P *= lista_primos[j]
	return(P)

# ''' recorre cada dupla de una lista e invierte su orden, osea (x,y) -> (y,x), 
# y devuelve una lista con las duplas invertidas '''
# def invertir_duplas(lista):
# 	nueva_lista = []
# 	for i in range(len(lista)):
# 		nueva_lista.append( lista[i][::-1] )
# 	return(nueva_lista)

# def ordenar_duplas(lista):
# 	return( invertir_duplas( sorted( invertir_duplas(lista) ) ) )

# lista_duplas = []
# for i in range(1,100000+1):
# 	lista_duplas.append( (rad(i),i) )

# lista_duplas = sorted(lista_duplas)

# print(lista_duplas[10000-1][1])
