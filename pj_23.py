from math import sqrt
from itertools import combinations

def sum_divisores(n):
	lista = []
	for i in range(1, int(sqrt(n)) + 1):
		if n%i == i:
			lista.append(i)
		elif n%i == 0:
			lista.append(i)
			lista.append(n//i)

	lista.remove(n)
	return(sum(sorted(set(lista))))


abundant = []
for i in range(1, 28123 + 1):
	if sum_divisores(i) > i:
		abundant.append(i)

combinaciones = list(combinations(abundant,2))

sumas = []

for i in abundant:
	suma = 2*i
	if suma < 28123:
		sumas.append(suma)

for i in combinaciones:
	suma = sum(i)
	if suma < 28123:
		sumas.append(suma)

sumas = list(set(sumas))

S = 0
for i in range(1,28123):
	if i not in sumas:
		S += i

print(S)

#4179871
#[Finished in 51.1s]
