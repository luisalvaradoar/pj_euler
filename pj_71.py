# def HCF_euclides(x, y):
#    while(y):
#        x, y = y, x % y

#    return x

# lista = []
# for d in range(1, 10 ** 4):
# 	for n in range(1, d):
# 		if HCF_euclides(n, d) == 1:
# 			lista.append((round(n / d, 3), n, d))

# print(len(lista))
import itertools

combi = list(itertools.permutations([0, 1, 2, 3, 4, 5]))

print(len(combi))