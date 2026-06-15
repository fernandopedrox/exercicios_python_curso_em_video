primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo_final = int(input("Digite o número de termos da PA: "))
for c in range(primeiro_termo, primeiro_termo + (termo_final - 1) * razao + razao, razao):
    print(c, end=" ")
