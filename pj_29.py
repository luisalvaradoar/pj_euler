'''realiza todas las combinaciones para a^b y las guarda en una lista'''
A = 100
B = 100
lista = []
for a in range(2, A + 1):
	for b in range(2, B + 1):
		lista.append(a ** b)

# se eliminan los elementos repetidos
lista = set(lista)

print(len(lista))