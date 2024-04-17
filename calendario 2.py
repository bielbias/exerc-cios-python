n1 = int(input("Indique o número existente de dias de um mês: "))

list1 = ["2 - Fevereiro", "28 Dias"]
list2 = ["30 Dias", "4 - Abril", "6 - Junho", "9 - Setembro", "11 - Novembro"]
list3 = ["31 Dias", "1 - Janeiro", "3 - Março", "5 - Maio", "7 - Julho", "8 - Agosto", "10 - Outubro", "12 - Dezembro"]


if n1 == 28:
    print(list1)
elif n1 == 30:
    print(list2)
elif n1 == 31:
    print(list3)
else:
    print("Número inválido")

