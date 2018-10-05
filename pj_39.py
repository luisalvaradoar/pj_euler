import math

def n_ternas(p):
	ternas = []
	cs = []
	for a in range(1, p//2):
		for b in range(1, p//2):
			c = math.sqrt(a**2 + b**2)
			disc = a + b + c
			if disc == p and not(c in cs):
				cs.append(c)
				ternas.append((a, b, int(c)))
	return(len(ternas))

sol = []
for p in range(1000):
	sol.append((n_ternas(p), p))

print(max(sol))