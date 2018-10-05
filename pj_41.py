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

''' la funcion nDigito recibe como parametro un numero entero de 1-9 
crea una lista 'digitos' con los digitos del 1 a n, luego crea todas 
permutaciones de esa lista, por ultimo une todas las n-adas y las guarda
en una lista ya como int, devuelve lista pandigitales '''
def nDigito(n):
	digitos = []
	for i in range(1, n + 1):
		digitos.append(str(i))

	permutaciones = list(itertools.permutations( digitos ))

	pandigitales = []
	for i in range(len(permutaciones)):
		P = ''
		for j in range(n):
			P += permutaciones[i][j]
		pandigitales.append(int(P))

	return(pandigitales)

xam = 0
for n in range(1,9):
	nPandigital = nDigito(n)
	nPandigital_primos = []
	for i in range(len(nPandigital)):
		if eratostenes(nPandigital[i]) > xam:
			xam = eratostenes(nPandigital[i])

print(xam)
