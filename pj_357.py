import math

def eratostenes( n ):
	if n == 1:
		return False
	else:
		for i in range( 2 , int(math.sqrt(n)) + 1 ):
			if n % i == 0:
				return False
		return True

def divisores(n):
	lista = []
	for i in range(1, int(math.sqrt(n)) + 1):
		if n%i == i:
			lista.append(i)
		elif n%i == 0:
			lista.append(i)
			lista.append(n//i)

	return(sorted(set(lista)))

def d_id(n):
	div = divisores(n)
	for d in div:
		N = d + n//d
		if not eratostenes(N):
			return False
	return True

# def d_id2(n):
# 	div = divisores(n)
# 	for d in range(len(div)//2):
# 		N = div[d] + n//div[d]
# 		print(N)
# 		if not eratostenes(N):
# 			return False

# 	return True
lista1 = []
for i in range(1,100):
	if d_id(i):
		lista1.append(i)
print(lista1)
