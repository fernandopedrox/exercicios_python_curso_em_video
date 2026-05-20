nomes = input("Digite seu nome completo: ")
maiusculo = nomes.upper()
minusculo = nomes.lower()
semespaco = nomes.replace(" ", "")
quantidade = len(semespaco)
primeiro = nomes.split()
print(f"""Nome com todas as letras maiúsculas: {maiusculo}, 
nome com todas as letras minúsculas: {minusculo}, 
quantidade de letras sem espaço: {quantidade},
primeiro nome: {primeiro[0]}""")
