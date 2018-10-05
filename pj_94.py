from math import sqrt

def HeronInt(x):
	A1 = (1/4) * (x + 1) * sqrt(3 * x**2 - 2 * x -1)
	A2 = (1/4) * (x - 1) * sqrt(3 * x**2 + 2 * x -1)
	if (A1 - int(A1)) == 0 or (A2 - int(A2)) == 0:
		return True
	else:
		return False

S = 0
for i in range(2, 333333333):
	if HeronInt(i) and (3*i - 1) < 10**9:
		S += 3*i + 1

print(S)