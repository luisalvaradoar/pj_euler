suma_de_cuadrados = 0
suma = 0

'''recorro los primeros 100 naturales calculando su cuadrado para luego sumarlo
a 'suma_de_cuadrados'. Y sumo los naturales en 'suma'
'''
for n in range(101):
	suma_de_cuadrados += n ** 2
	suma += n

print(suma ** 2 - suma_de_cuadrados)