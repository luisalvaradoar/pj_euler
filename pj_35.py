from math import sqrt

def rotcir(ns):
	lista = [ns]
	for i in range(len(ns) - 1):
		a = ns[0]
		ns = ns[1:len(ns)+1]
		ns += a
		lista.append(ns)

	return(lista)

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def primo_circular(n):
	rotaciones = rotcir(str(n))
	for j in rotaciones:
		if not eratostenes(int(j)):
			return(False)
	return(True)

cont = 0
for i in range(2,10**6):
	if eratostenes(i):
		if primo_circular(i):
			cont += 1

print(cont)

#55
#[Finished in 11.9s]