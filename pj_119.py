import math

def suma_dig(n):
	n = str(n)
	suma_dig = 0
	for i in range(len(n)):
		suma_dig += int(n[i])
	return(suma_dig)

cont = 10
for n in range(614656,10**9):
	b = suma_dig(n)
	if b != 1:
		i = math.log(n,b)
		disc = i - math.floor(i)
		if disc == 0:
			print(cont, n, b, int(i))
			cont += 1
			if cont == 30:
				break