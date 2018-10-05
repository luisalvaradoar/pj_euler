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

def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

def phi(n):
	cont = 0
	for i in range(1,n):
		if mcd(n,i) == 1:
			cont += 1
	return(cont)


def phi2(n):
	if eratostenes(n) != 0:
		return(n-1)
	lista_primos = []
	P = n
	for i in range(round(n/2)+1):
		if eratostenes(i) != 0:
			if n % eratostenes(i) == 0:
				lista_primos.append(i)
	for j in range(len(lista_primos)):
		P *= 1 - 1 / lista_primos[j]
	return(int(P))


xam = 0
nxam = 0

for i in range(2,10 ** 6):
	disc = i / phi2(i)
	if disc > xam:
		xam = disc
		nxam = i

print(nxam)
print(xam)