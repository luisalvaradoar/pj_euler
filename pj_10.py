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

# corre la la funcion eratostenes un numero indefinido de veces, el contador 'i' se aumenta en +1 cada vez que se determina un numero 'p' primo.
# cuando el contador 'i' llega al maximo imprime el numero 'p' y termina el ciclo
p = 1
suma = 0
while True:
	if eratostenes( p ) != 0:
		suma += p
		p += 1
	else:
		p += 1
	if p > 2000000:
		print( suma )
		break