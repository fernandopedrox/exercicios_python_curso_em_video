maior = 0
menor = 0
for c in range(5):
    peso = float(input("Digite seu peso: "))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
print(f"O maior peso foi {maior:.1f}Kg e o menor peso foi de {menor:.1f}Kg.")