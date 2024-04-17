#triangulo
l1 = float(input("Informe o primeiro lado do triângulo: "))
l2 = float(input("Informe o segundo lado do triângulo: "))
l3 = float(input("Informe o terceiro lado do triângulo: "))

if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        print("Você me indicou um triângulo equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Você me indicou um triângulo isósceles.")
    else:
        print("Você me indicou um triângulo escaleno.")
else:
    print("Os números indicados não viram um triângulo.")

