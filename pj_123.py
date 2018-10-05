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

# dado un entero, encuentra el siguiente primo
def sig_primo( n ):
	n += 1
	while(True):
		if eratostenes( n ) != 0:
			return( n )
			break
		else:
			n += 1

i = 1
n = 1
while(True):
	p = sig_primo(i)
	disc = ( ( p - 1 ) ** n + ( p + 1 ) ** n ) % (p ** 2)
	if disc > 10 ** 10:
		print(n)
		break
	else:
		i = p
		n += 1