from math import sqrt

def suma_divisores(n):
	lista = []
	for i in range(1, int(sqrt(n)) + 1):
		if n%i == i:
			lista.append(i)
		elif n%i == 0:
			lista.append(i)
			lista.append(n//i)

	lista.remove(n)
	return(sum(sorted(set(lista))))

def cadena(n):
	cad = [n]
	a = n
	while True:
		b = suma_divisores(a)
		if b > 10**6 or b == 1:
			return(False, 0, 0)
		if b not in cad:
			cad.append(suma_divisores(a))
			a = b
		else:
			return(True, cad, len(cad))


cumplen = []
analizados = []
for i in range(10**0, 10**5):
	A = cadena(i)
	if A[0]:
		cumplen.append([A[2], min(A[1])])

print(max(cumplen))


#[55, 1184]