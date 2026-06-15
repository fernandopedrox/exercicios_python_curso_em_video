soma_idade = 0
idade_velho = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0
for c in range(4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ").lower().strip()
    soma_idade += idade
    if sexo == "m":
        if idade_velho == 0:
            idade_velho = idade
            nome_homem_mais_velho = nome
        else:
            if idade > idade_velho:
                idade_velho = idade
                nome_homem_mais_velho = nome
    elif sexo == "f":
        if idade < 20:
            mulheres_menos_20 += 1
    else:
        print("Sexo inválido. Digite M para masculino ou F para feminino. (Você disperdiçou um dos cadastros)")
media = soma_idade / 4
print(f"A média de idade do grupo é de {media} anos. O homem mais velho é {nome_homem_mais_velho} com {idade_velho} anos. E o total de mulheres com menos de 20 anos é de {mulheres_menos_20} mulher(es).")
