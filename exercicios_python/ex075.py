c = numero3 = 0
numeros = ()
pares = ()
while True:
    n = int(input("Digite um número: "))
    numeros += (n,)
    c += 1
    if n % 2 == 0:
        pares += (n,)
    if c == 4:
        break
numero9 = numeros.count(9)
if 3 in numeros:
    numero3 = numeros.index(3)
print(f"""O valores que você digitou foram {numeros}
O valor 9 apareceu {numero9} vezes
Os números pares foram {pares}""")
if numero3 != 0:
    print(f"O valor 3 apareceu na {numero3 + 1}ª posição")
else:
    print("O valor 3 nao foi digitado em nenhuma posição")
