def dig_str(n):
	lista = []
	st = str(n)
	for i in range(len(st)):
		lista.append(st[i])
	return(sorted(lista))

def comparador_de_digitos(x,y):
	if dig_str(x) == dig_str(y):
		return(1)
	else:
		return(0)

N = 1
while(True):
	if comparador_de_digitos(N, 2 * N) == 1 and comparador_de_digitos(N, 3 * N) == 1 and comparador_de_digitos(N, 4 * N) == 1 and comparador_de_digitos(N, 5 * N) == 1 and comparador_de_digitos(N, 6 * N) == 1:
		print(N)
		break
	else:
		N += 1