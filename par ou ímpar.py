n1 = int(input("Digite um número inteiro positivo: "))

x1 = n1 % 2

if n1 < 0:
    print("Insira um número positivo.")
elif x1 == 1:
    print("Seu número ",n1," é ímpar")
elif x1 == 0:
    print("Seu número ",n1," é par")
