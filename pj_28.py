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

A = N_by_N(1001)
print(sum(A) + 1)

#669171001
#[Finished in 0.1s]