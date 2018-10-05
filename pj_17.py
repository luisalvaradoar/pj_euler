d1 = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
d2 = {'10':'ten', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}
d3 = {'11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}

def numero_a_palabra(n):
	ns = str(n)
	palabra = []

	if len(ns) == 1:
		palabra.append(d1[ns[0]])
		return(palabra)

	if ns in d2:
		palabra.append(d2[ns])
		return(palabra)

	if len(ns) < 3:
		ns = '0' + ns

	if ns[2] == '0' and ns[1] == '0':
		palabra.append(d1[ns[0]])
		palabra.append('hundred')
		return(palabra)

	if ns[0] != '0':
		palabra.append(d1[ns[0]])
		palabra.append('hundred')

	if ns[2] == '0':
		palabra.append('and')
		palabra.append(d2[ns[1] + '0'])
	elif ns[-2::] in d3:
		if ns[0] == '0':
			palabra.append(d3[ns[-2::]])
		else:
			palabra.append('and')
			palabra.append(d3[ns[-2::]])
	elif ns[1] == '0':
		palabra.append('and')
		palabra.append(d1[ns[2]])
	else:
		if ns[0] == '0':
			palabra.append(d2[ns[1] + '0'])
			palabra.append(d1[ns[2]])
		else:
			palabra.append('and')
			palabra.append(d2[ns[1] + '0'])
			palabra.append(d1[ns[2]])

	return(palabra)


suma = 0
for i in range(1,1000):
	N = numero_a_palabra(i)
	for j in range(len(N)):
		suma += len(N[j])

print(suma + 11)