from random import randint
numeros_aleatorios = ()
c = 0
while True:
    numeros_aleatorios += (randint(0, 20),)
    c += 1
    if c == 5:
        break
maior = max(numeros_aleatorios)
menor = min(numeros_aleatorios)
print(f"""O números sorteados foram {numeros_aleatorios}
Sendo o maior {maior} e o menor {menor}""")
