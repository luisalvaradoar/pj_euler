fib1 = 1
fib2 = 2
temp = 0 
cont = 3

while(True):
	temp = str(fib2)
	if len(temp) == 1000:
		break
	temp = fib1 + fib2
	fib1 = fib2
	fib2 = temp
	cont += 1

print(cont)
print(temp)
