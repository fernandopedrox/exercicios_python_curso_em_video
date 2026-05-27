primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
for c in range(primeiro_termo, primeiro_termo + (10 - 1) * razao + 1, razao):
    print(c, end=" ")