while True:
    numero = int(input("Digite um número que deseja converter: "))
    opcao = int(input("""Escolha uma das seguintes opções para a conversão:
    1 = binário
    2 = octal
    3 = hexadecimal
    : """))
    if opcao > 3 or opcao < 1:
        print("Opção inválida!")
    else:
        if opcao == 1:
            conversao = bin(numero)
        elif opcao == 2:
            conversao = oct(numero)
        else:
            conversao = hex(numero)
        print(conversao[2:])
        continuar = input("Deseja continuar: (S/N)").lower().strip()
        if continuar == "n":
            break
