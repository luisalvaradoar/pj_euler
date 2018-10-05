from math import sqrt

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def contar_dig(n):
	C = []
	for i in range(10):
		x = str(n).count(str(i))
		if x > 1:
			C.append(i)

	return(C)

def familiaP(p, dig_rep):
	familia = []
	for i in range(10):
		pi = int(str(p).replace(str(dig_rep), str(i)))
		if eratostenes(pi) and len(str(pi)) == len(str(p)):
			familia.append(pi)

	return(familia)


def main():
	for i in range(10**6):
		if eratostenes(i):
			X = contar_dig(i)
			if len(X) > 0:
				for j in X:
					Y = familiaP(i, j)
					if len(Y) == 8:
						return(min(Y))

print(main())

#121313
#[Finished in 1.3s]