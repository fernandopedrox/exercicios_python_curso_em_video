n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 > n2:
    maior = n1
    menor = n2
    print(f"O número primeiro número {maior} é maior que o segundo número {menor}.")
elif n2 > n1:
    maior = n2
    menor = n1
    print(f"O segundo número {maior} é maior que o primeiro número {menor}.")
else:
    print("Os números são iguais.")
