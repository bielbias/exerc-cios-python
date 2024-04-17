n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
sinal = str(input("Qual das seguintes operações você quer realizar: + - * /: "))

if sinal == "+":
    print("A soma dos seus números é =", n1 + n2)
elif sinal == "-":
    print("A subtração dos seus números é =", n1 - n2)
elif sinal == "*":
    print("A multiplicação dos seus números é =", n1 * n2)
elif sinal == "/":
    print("A divisão dos seus números é =", n1 / n2)
else: 
    print("Digite um sinal válido")

