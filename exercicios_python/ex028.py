from random import randint
bot = randint(0, 5)
player = int(input("Digite um número entre 0 e 5: "))
if player <0 or player >5:
    print("Digite apenas números dentro da faixa citada")
else:
    if player == bot:
        print(f"Parabéns, você acertou! Eu escolhi o número {bot} e você escolheu o número {player}")
    else:
        print(f"Que pena, você errou! Eu escolhi o número {bot} e você escolheu o número {player}")
