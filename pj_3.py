import math

'''criba de eratostenes para probar si un numero 'n' es primo.
Prueba a n mod k para k < sqrt(n) '''
def eratostenes( n ):
	if n == 1:
		return( 0 )
	else:
		for i in range( 2 , int( math.floor( math.sqrt( n ) ) ) + 1 ):
			if n % i == 0:
				return( 0 )
		return( n )

'''recorre la lista desde la raiz cuadrada del numero en cuestion hasta 0,
comprobando si es primo, en caso lo sea comprueba si divide al numero el primer 
primo que lo divida sera el mas grande, ya que se recorre la lista al revez '''
numero = 600851475143
i = int( math.floor( math.sqrt( numero ) ) )
for j in range(i,0,-1):
	if eratostenes(j) != 0:
		if numero % j ==0:
			print(j)
			break