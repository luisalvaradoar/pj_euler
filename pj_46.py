from math import sqrt

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def Goldbach(n):
	global primos
	a = 1
	while n - 2*a**2 > 0:
		if eratostenes(n - 2*a**2):
			return True
		a += 1
	return False

for i in range(5,10000,2):
	if not eratostenes(i):
		if not Goldbach(i):
			print(i)
			break

#5777
#[Finished in 0.1s]