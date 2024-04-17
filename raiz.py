n1 = int(input('Informe um número para fazer o cálculo da raiz: '))

if n1 < 0:
    print('Número inválido')
else:
    import math 
    x = math.sqrt(n1)
    print(x)
