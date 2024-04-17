print('Cachorro quente - 100 - 1,20\nBauru simples - 101 - 1,30\nBauru com ovo - 102 - 1,50\nHamburguer - 103 - 1,20\nX burguer - 104 - 1,70\nSuco - 105 - 2,20\nRefrigerante - 106 - 1,00')
n1 = int(input('Informe o código do alimento: '))
n2 = int(input('Digite a quantidade do produto: '))

if n1 == 100:
    print('Você irá pagar: ', 1.20 * n2)
elif n1 == 101:
    print('Você irá pagar: ', 1.30 * n2)
elif n1 == 102:
    print('Você irá pagar: ', 1.50 * n2)
elif n1 == 103:
    print('Você irá pagar: ', 1.20 * n2)
elif n1 == 104:
    print('Você irá pagar: ', 1.70 * n2)
elif n1 == 105:
    print('Você irá pagar: ', 2.20 * n2)
elif n1 == 106:
    print('Você irá pagar: ', 1.00 * n2)
else:
    print('Código inválido!')
