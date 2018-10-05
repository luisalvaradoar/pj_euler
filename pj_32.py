import itertools
# generamos una lista con todos los pandigitales de 1-9
pandigitales = list(itertools.permutations( ['1', '2', '3', '4', '5', '6', '7', '8', '9'] ))

'''recibe una lista de nueve digitos, recorre la lista concatenando los elementos
al final devuelve el numero unido'''
def unir_pandigital(n):
	numero = ''
	for i in n:
		numero += i
	return(numero)

def operar_pandigital(Np, i):
	Np_unido = unir_pandigital(Np)

	if i == 1:
		a = int(Np_unido[0])
		b = int(Np_unido[1:4])
		c = int(Np_unido[4:9])
		if (a * b == c):
			return(True, a, b ,c)
		else:
			return(False, 0)
	elif i == 2:
		a = int(Np_unido[0])
		b = int(Np_unido[1:5])
		c = int(Np_unido[5:9])
		if (a * b == c):
			return(True, a, b ,c)
		else:
			return(False, 0)
	elif i == 3:
		a = int(Np_unido[0:2])
		b = int(Np_unido[2:5])
		c = int(Np_unido[5:9])
		if (a * b == c):
			return(True, a, b ,c)
		else:
			return(False, 0)
	elif i == 4:
		a = int(Np_unido[0:3])
		b = int(Np_unido[3:5])
		c = int(Np_unido[5:9])
		if (a * b == c):
			return(True, a, b ,c)
		else:
			return(False, 0)
	elif i == 5:
		a = int(Np_unido[0:4])
		b = int(Np_unido[4])
		c = int(Np_unido[5:9])
		if (a * b == c):
			return(True, a, b, c)
		else:
			return(False, 0)

cumplen = []
for i in range(len(pandigitales)):
	for j in range(1,6):
		x = pandigitales[i]
		y = operar_pandigital(x, j)
		if y[0]:
			cumplen.append( y[3] )

print(sum(set(cumplen)))