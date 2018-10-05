import math

def sum_fac_dig(n):
	S = 0
	ns = str(n)
	for i in range(len(ns)):
		S += math.factorial(int(ns[i]))
	return(S)

n = 0
while(True):
	if sum_fac_dig(n) == n:
		print(n)
		n += 1
	else:
		n += 1

# al parecer los unicos dos numeros que se pueden expresar como la suma 
# de los factoriales de sus digitos son 1, 2, 145 y 40585