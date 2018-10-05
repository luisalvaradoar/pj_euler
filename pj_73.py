def HCF_euclides(x, y):
   while(y):
       x, y = y, x % y

   return x

lista = []
for d in range(1, 12000):
	for n in range(1, d):
		if HCF_euclides(n, d) == 1:
			lista.append((round(n / d, 3), n, d))


pos_13 = sorted(lista).index((round(1 / 3, 3), 1, 3))
pos_12 = sorted(lista).index((round(1 / 2, 3), 1, 2))

print(pos_12 - pos_13 - 1)