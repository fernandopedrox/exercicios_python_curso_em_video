numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
digito = -1
while True:
    digito = int(input("Digite um número entre 0 e 20: "))
    if 0 <= digito <= 20:
        break
print(f"Você digitou o número {numeros[digito]}")
