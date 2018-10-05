from math import sqrt, floor

def sqrtN(x):
	a0 = floor(sqrt(x))
	an = []
	sN = (sqrt(x) - a0)**(-1)
	for i in range(20):
		ai = floor(sN)
		an.append(ai)
		sN = (sN - floor(sN))**(-1)

	return an

print(sqrtN(201))