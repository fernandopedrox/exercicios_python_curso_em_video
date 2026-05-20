import random
aluno1 = input("Digite seu nome: ")
aluno2 = input("Digite seu nome: ")
aluno3 = input("Digite seu nome: ")
aluno4 = input("Digite seu nome: ")
escolha = random.choice([aluno1, aluno2, aluno3, aluno4])
print(f"O aluno escolhido para apagar o quadro foi: {escolha}")
