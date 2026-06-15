from random import randint
player = 1
bot = 0
while player != bot:
    bot = randint(0, 10)
    player = int(input("Tente adivinhar o númer que estou pensando (entre 0 e 10): "))
    if player != bot:
        print(f"Tente novamente! Eu escolhi o número {bot} e você o número {player}")
print(f"Parabéns! você venceu! eu escolhi o número {bot} e você o número {player}")