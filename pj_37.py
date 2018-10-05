import math
# criba de eratostenes para probar si un numero 'n' es primo. Prueba a n mod k para k < sqrt(n)
def eratostenes(n):
	if n == 1:
		return(0)
	else:
		for i in range(2 , int(math.floor(math.sqrt(n))) + 1):
			if n % i == 0:
				return(0)
		return(n)

def trunc_iz_de(n): # n es primo
	ns = str(n)
	for i in range(len(ns)):
		ns = ns[1 - len(ns)::] # esto trunca el primer digito
		if eratostenes(int(ns)) == 0:
			return(False)
	return(True)

def trunc_de_iz(n): # n es primo
	ns = str(n)
	for i in range(len(ns)):
		if len(ns) > 1:
			ns = ns[0:len(ns) - 1] # esto trunca el primer digito
		if eratostenes(int(ns)) == 0:
			return(False)
	return(True)

i = 8
cont = 0
cumplen = []
while(True):
	if eratostenes(i) != 0:
		if trunc_iz_de(i) and trunc_de_iz(i):
			cumplen.append(i)
			i += 1
			cont += 1
			if cont == 11:
				break
		else:
			i += 1
	else:
		i += 1

print(cumplen)
print(sum(cumplen)) 