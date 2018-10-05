import math

def nth(N):
	i = 1
	ns = str(N)
	d = len(ns)
	while (i**d) <= N:
		if (i**d) == N:
			return True
		else:
			if N % 2 == 0:
				i += 1
			else:
				i += 2
	return(False)


cont = 0
for i in range(10 ** 7):
	if nth(i):
		cont += 1
		print(cont, i)
