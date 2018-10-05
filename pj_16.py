import math

n = 2 ** 1000
suma = 0
# se calcula el orden del numero en potencia de 10.
M = math.floor( math.log10( n ) ) + 2

M = int( M )
# la parte ( n % 10 ** i ) // 10 ** (i-1) divide al numero en la cifra i
for i in range(1, M  ,1):
	suma += ( n % 10 ** i ) // 10 ** (i-1)

print(suma)