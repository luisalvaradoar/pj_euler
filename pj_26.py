def div1(n):
	r = []
	L = [10]
	u = 10
	while True:
		if u%n == u:
			u = u*10
			while u%n == u:
				r.append(0)
				u *= 10
			if u not in L:
				L.append(u)
				r.append(u//n)
				u %= n
				if u == 0:
					return r
			else:
				return r
		else:
			r.append(u//n)
			u %= n

			if u == 0:
				return r

T = []
for i in range(2,1001):
	T.append((len(div1(i)),i))

print(max(T))

#(983, 983)
#[Finished in 0.4s]