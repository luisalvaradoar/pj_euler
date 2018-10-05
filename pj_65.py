from fractions import Fraction

def sucesionE(n):
	suc = [1, 2]

	i = 2
	while len(suc) <= n:
		suc.append(1)
		suc.append(1)
		suc.append(2*i)
		i += 1

	return suc[0:n]

def fracciones(a, ans):
	ans = ans[::-1]
	ai1 = Fraction(1, ans[0])
	A = ans[1] + ai1
	ans.remove(ans[0])
	ans.remove(ans[0])
	for i in ans:
		ax = i + Fraction(1, A)
		A = ax

	return(2 + Fraction(1, A))

lista = sucesionE(99)
frac = str(fracciones(2, lista)).split('/')

S = 0
for i in range(len(frac[0])):
	S += int(frac[0][i])

print(S)
#272
#[Finished in 0.1s]