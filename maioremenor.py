#maioremenor
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O primeiro número",n1,"é o maior número")
elif n2 > n1 and n2 > n3:
    print("O segundo número",n2,"é o maior número")
else:
    print("O terceiro número",n3,"é o maior número")
    
if n1 < n2 and n1 < n3:
    print("O primeiro número",n1,"é o menor número")
elif n2 < n1 and n2 < n3:
    print("O segundo número",n2,"é o menor número")
else:
    print("O terceiro número",n3,"é o menor número")

