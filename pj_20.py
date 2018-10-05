import math

n = math.factorial( 100 )
suma = 0

M = math.floor( math.log10( n ) ) + 2

M = int( M )

for i in range( 1 , M  , 1 ):
	suma += ( n % 10 ** i ) // 10 ** ( i - 1 )

print( suma )