maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
print(f"O maior peso foi {maior:.1f}Kg e o menor peso foi de {menor:.1f}Kg.")