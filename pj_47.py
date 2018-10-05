from math import sqrt

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def fac_prim(n):
	R = []
	if eratostenes(n):
		R.append(n)
		return R
	for p in range(2, int(sqrt(n)) + 1):
		if eratostenes(p):
			while n%p ==0:
				if n%p == 0:
					n = n//p
					R.append(p)
					if eratostenes(n):
						R.append(n)
						return(R)

rep = 4
cont = 0
for i in range(2,1000000):
	f = len(set(fac_prim(i)))
	if f == rep:
		cont += 1
	else:
		cont = 0

	if cont == rep:
		print(i - rep + 1)
		break

#134043
#[Finished in 4.6s]