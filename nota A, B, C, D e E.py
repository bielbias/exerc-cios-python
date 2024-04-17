n1 = int(input('Informe uma nota de 0 a 100: '))

if n1 >= 86 and n1 <= 100:
    print('Sua nota é A')
elif n1 < 86 and n1 >= 61:
    print('Sua nota é B')
elif n1 < 61 and n1 >= 36:
    print('Sua nota é C')
elif n1 < 36 and n1 >= 1:
    print('Sua nota é D')
elif n1 > 100:
    print('Número inválido')
else:
    print('Sua nota é E')
