''' este grupo de numeros tiene un bucle, digamos que hacemos el algoritmo para "x" numero
la sucesion comenzara con (2, 2x, 2, ... , 2, 2x, 2, ...) donde ... es un bucle
entonces cuando 2x aparezca por segunda vez cortamos alli la sucesion y sacamos
el maximo '''

def algoritmo(a):
	lista = []
	i = 0
	cont = 0
	xam = 0
	n = 0
	while(True):
		r = ((a - 1) ** n + (a + 1) ** n ) % (a ** 2)
		lista.append(r)
		i += 1
		n += 1
		if r == 2 * a:
			cont += 1
			if cont == 2:
				lista = lista[0: i - 2]
				xam = max(lista)
				break
	return(xam)

total = 0
for a in range(3, 1000 + 1):
	total += algoritmo(a)

print(total)