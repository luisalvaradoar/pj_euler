from fractions import Fraction

def sqrt2(it):
	dem = 2
	for i in range(it):
		dem = 2 + Fraction(1, dem)

	return(str(1 + 1/dem).split('/'))

cont = 0
for i in range(1, 1000+1):
	N = sqrt2(i)
	if len(N[0]) > len(N[1]):
		cont += 1

print(cont)