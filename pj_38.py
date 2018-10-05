def pandigitalQ(ns):
	for i in range(1,10):
		if ns.count(str(i)) != 1:
			return(False)

	return(True)


def pan_mul(n):
	i = 1
	ns = str(n)
	while(True):
		i += 1
		ns += str(n * i)
		for j in range(1,10):
			if ns.count(str(j)) > 1:
				return(False,0)
			if len(ns) == 9:
				if pandigitalQ(ns):
					return(True,int(ns))

cumplen = []
for i in range(1,10**4):
	val = pan_mul(i)
	if val[0]:
		cumplen.append(val[1])

print(max(cumplen))