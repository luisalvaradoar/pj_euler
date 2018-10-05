import math
'''Cuando n = i mod 0, esto es i|n, suma uno a d. Los divisores de n
no seran mayores a sqrt(n), poer eso el range llega hasta alli'''
def divisores( n ):
	d = 0
	for i in range( 1 , round( math.sqrt(n) )  ):
		if n % i == 0:
			d += 1
	return(2*d)

# se usa la forma cerrada de 1 + 2 + 3 + ... + n para el n-esimo numero triangular
def ntriangular( n ):
	return( ( n + 1 ) * n // 2 )

i = 1
while( True ):
	a = divisores( ntriangular( i ) )
	if a > 500:
		print( ntriangular( i ) )
		break
	else:
		i += 1