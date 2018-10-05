def palindromoQ(n):
	ns = str(n)
	if ns == ns[::-1]:
		return(True)
	else:
		return(False)

def Lychrel(n):
	cont = 0
	while(True):
		ni = int(str(n)[::-1])
		n = n + ni
		cont += 1
		if palindromoQ(n):
			return(n, cont)
		elif cont == 50:
			return(True, 0)

C = 0
for i in range(10000 + 1):
	x = Lychrel(i)
	if x[0] == True:
		C += 1

print(C)