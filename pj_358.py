def rotcir(ns):
	lista = [ns]
	for i in range(len(ns) - 1):
		a = ns[0]
		ns = ns[1:len(ns)+1]
		ns += a
		lista.append(ns)

	return(lista)

def cyclic_number(ns):
	rotaciones = rotcir(ns)
	for n in range(1, len(ns)):
		Ns = str(n*int(ns))

		while len(Ns) != len(ns):
			Ns = '0' + Ns

		if Ns not in rotaciones:
			return False

	return True

import itertools

def per_n(n):
	lista1 = list(itertools.product('0123456789',repeat=n))

	lista2 = []
	for i in lista1:
		n = ''
		for j in range(len(i)):
			n += i[j]
		lista2.append(n)

	return(lista2)


i = 8
agregado = per_n(i)
for j in agregado:
	ns = '00000000137' + j + '56789'
	if cyclic_number(ns):
		print(ns)
		break