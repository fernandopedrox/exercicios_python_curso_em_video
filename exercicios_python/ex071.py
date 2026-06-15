nota50 = nota20 = nota10 = nota1 = total =0
sacar = int(input("Digite quanto deseja sacar: "))
total = sacar
while True:
    while sacar >= 1:
        if sacar >= 50:
            nota50 = sacar // 50
            sacar -= 50 * nota50
        elif sacar >= 20:
            nota20 = sacar // 20
            sacar -= 20 * nota20
        elif sacar >= 10:
            nota10 = sacar // 10
            sacar -= 10 * nota10
        elif sacar >= 1:
            nota1 = sacar // 1
            sacar -= 1 * nota1
    break
print(f"""O dinheiro {total} deu um total de cedulas foi de:
cedulas de 50: {nota50}
cedulas de 20: {nota20}
cedulas de 10: {nota10}
cedulas de 1: {nota1} """)

#ou pode ser do jeito a baixo:
#Da pra fazer o com for, que é bem mais fácil, porém o exercício é de while
valor = int(input("Digite o valor a ser sacado: "))
nota = 50
while True:
    if valor >= nota:
        qnotas = valor // nota
        valor -= qnotas * nota
        print(f"O total de notas de {nota}: {qnotas}")
    else:
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        else:
            break
