from random import randint
c = 0
escolhas = ['impar', 'par']
imparPar = ""
imparoupar = ""
while True:
    player = int(input("Digite um número: "))
    while imparPar not in escolhas:
        imparPar = str(input("Escolha impar ou par: ")).strip().lower()
        if imparPar not in escolhas:
            print("Digite corretamente!")
    bot = randint(1, 10)
    soma = bot + player
    imparoupar = "par" if soma % 2 == 0 else "impar"
    if imparPar == imparoupar:
        print(f"Jogador venceu! Você escolheu {player} e o computador {bot}. O total deu {player + bot} que da {imparoupar}")
        c += 1
        imparPar = ""
    else:
        print(f"Você perdeu! o jogador escolheu {player} e o computador {bot}. O total deu {player + bot} que da {imparoupar}")
        break
print(f"Você venceu {c} vezes")
