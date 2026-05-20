nome = input("Digite seu nome completo: ").upper().strip()
numero_de_letras_a = nome.count("A")
primeira_letra_a = nome.find("A")
ultima_letra_a = nome.rfind("A")
print(f"""O nome em maiúsculo é: {nome}
      O número de letras A é: {numero_de_letras_a}
      A primeira letra A aparece na posição: {primeira_letra_a}
      A última letra A aparece na posição: {ultima_letra_a}""")
