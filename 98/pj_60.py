from itertools import combinations, permutations
from math import sqrt

def eratostenes(n):
	if n == 1:
		return False
	else:
		for i in range(2 , int(sqrt(n))+ 1):
			if n % i == 0:
				return False
		return True

def comb2(n1, n2):
	N1 = int(str(n1) + str(n2))
	N2 = int(str(n2) + str(n1))
	if eratostenes(N1) and eratostenes(N2):
		return True
	else:
		return False

def analizador(combinacion):
	parejas = list(combinations(combinacion, 2))
	for pq in parejas:
		if not comb2(pq[0], pq[1]):
			return False

	return True

listaP = []
for p in range(3, 500):
	if eratostenes(p):
		listaP.append(p)

comb = list(combinations(listaP, 5))

for i in comb:
	if analizador(i):
		print(i)
		break
