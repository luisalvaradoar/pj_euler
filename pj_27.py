import math
# criba de eratostenes para probar si un numero 'n' es primo. Prueba a n mod k para k < sqrt(n)
def eratostenes( n ):
	n = abs(n)
	if n == 1:
		return( 0 )
	else:
		for i in range( 2 , int( math.floor( math.sqrt( n ) ) ) + 1 ):
			if n % i == 0:
				return( 0 )
		return( n )


''' recorre desde n = 0 la forma cuadratica n^2 + a*n + b, cuando ni es primo
suma 1 a cont, cuando algun ni no sea primo para el ciclo y devuelve cont '''
def cont_euler(a,b):
	n = 0
	cont = 0
	while(True):
		abn = n ** 2 + a * n + b
		if eratostenes(abn) == 0:
			break
		else:
			cont += 1
			n += 1

	return(cont)


xam = 0
A = 0
B = 0
for a in range(-10000, 10000 + 1):
	for b in range(-10000, 10000 + 1):
		if cont_euler(a,b) > xam:
			xam = cont_euler(a,b)
			A = a
			B = b

print(A)
print(B)
print(xam)
print(A * B)
