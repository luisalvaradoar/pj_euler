import math

def suma_dig(N):
	suma = 0
	M = int( math.floor( math.log10( N ) ) + 2 )
	for i in range(1, M  ,1):
		suma += ( N % 10 ** i ) // 10 ** (i-1)
	return(suma)

xam = 0
a0 = 0
b0 = 0
for a in range(1,100):
	for b in range(1,100):
		n = a ** b 
		comp = suma_dig( n )
		if comp > xam:
			xam = comp
			a0 = a
			b0 = b


print(xam,a,b)