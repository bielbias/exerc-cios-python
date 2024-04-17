n1 = int(input("Informe o primeiro número para comparar: "))
n2 = int(input("Informe o segundo número para comparar: "))

if n1 > n2:
    print("O número",n1,"é maior que o",n2)
elif n2 > n1:
    print("O número",n2,"é maior que o",n1)
else: 
    print("Os números são iguais")
