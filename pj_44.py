from math import sqrt

def Pn(n):
	return n*(3*n-1)//2

def PnQ(n):
	disc = (1 / 6) * (1 + sqrt(1 + 24 * n))
	if disc - int(disc) == 0:
		return True
	else:
		return False

listaPn = []
for i in range(1,10000):
	listaPn.append(Pn(i))

for Pj in listaPn:
	for k in range(listaPn.index(Pj)):
		Pk = listaPn[k]
		if PnQ(Pj + Pk) and PnQ(Pj - Pk):
			print(Pj, Pk, Pj-Pk)

#7042750 1560090 5482660
#[Cancelled]