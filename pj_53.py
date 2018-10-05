import math

def nCr(n,r):
	if r > n:
		return(0)
	else:
		return( (math.factorial( n )) // (math.factorial( r ) * math.factorial( n - r ) )  )

contador = 0
for n in range(101):
	for r in range(101):
		if nCr(n,r) > 1000000:
			contador += 1

print(contador)