parar = 0
contador = 0
acumulador = 0
maior = 0
menor = 0
while parar == 0:
    n = int(input("Digite um número inteiro: "))
    acumulador += n
    if contador == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    contador += 1
    continuar = input("Deseja continuar? [S/N]: ").lower().strip()
    if continuar == "n":
        parar = 1
    else:
        print("OK")
media = acumulador / contador
print(f"Você digitou {contador} números e a média foi {media:.2f} o maior número foi {maior} e o menor foi {menor}")