from itertools import permutations
from math import sqrt

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def perN(n):
	lista = []
	P = list(permutations(str(n)))
	for i in P:
		ns = ''
		for j in i:
			ns += j
		lista.append(int(ns))

	return lista

P_primos = []
for i in range(1000, 10000):
	if eratostenes(i):
		P_primos.append(i)

for i in P_primos:
	Per_i = perN(i)
	for j in range(P_primos.index(i) + 1, len(P_primos)):
		p1 = i
		p2 = P_primos[j]
		p3 = 2*p2 - p1
		if p3 in P_primos and p3 in Per_i and p2 in Per_i:
			print(p1, p2, p3)

#2969 6299 9629
#[Finished in 10.5s]