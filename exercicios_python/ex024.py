nome = input("Digite seu nome completo: ").upper()
nome = nome.split()
primeiro_nome = nome[0]
print("SANTO" in primeiro_nome)

#ou pode-se usar o comando startswith para verificar se o nome começa com a palavra "SANTO"
print(primeiro_nome.startswith("SANTO"))
