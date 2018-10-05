import itertools
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



n = 4
d = 1
listaP = [1,2,3]
lista1 =[]

for i in range(n):
	lista2 = lista1.append(str(d))
	listaP += lista2

for j in range(10):
	lista2 = lista1.append(str(j))



print(listaP)
listaP += [4,5]
print(listaP)
