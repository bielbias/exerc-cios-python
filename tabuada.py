n1 = int(input('Informe um valor entre 1 a 10:  '))

if (n1 < 0 or n1 > 10):
	print('Digite um numero valido de 1 até 10')
else:
	for i in range(11):
		print(i*n1)
