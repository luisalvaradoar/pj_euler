from math import sqrt

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def esquinas(a):
	N = a**2
	lista = [N]
	for i in range(1,4):
		N = N - (a - 2) - 1
		lista.append(N)

	return lista

def N_by_N(N):
	lista = []
	for i in range(3, N+1, 2):
		for j in esquinas(i):
			lista.append(j)

	return lista

def spiral(n):
	A = N_by_N(2*n + 1)
	primos = 0
	for p in A:
		if eratostenes(p):
			primos += 1

	e = primos / (len(A)+1)
	return(round(e,4))


for i in range(10, 100):
	print(spiral(i))