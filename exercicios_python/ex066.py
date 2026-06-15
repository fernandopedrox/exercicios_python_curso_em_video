soma = contador = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    contador += 1
print(f"A soma foi de {soma} e a quantidade de números digitados foi {contador}")
