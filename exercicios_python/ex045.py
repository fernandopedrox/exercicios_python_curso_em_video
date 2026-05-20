from random import choice
while True:
    escolhas = ['pedra', 'papel', 'tesoura']
    bot = choice(escolhas)
    jogador = input('Escolha entre: pedra, papel e tesoura: ').lower().strip()
    if jogador not in escolhas:
        print('Escolha inválida, tente novamente.')
    else:
        if jogador == bot:
            print(f'Empate! O computador escolheu {bot.upper()} e o jogador escolheu {jogador.upper()}')
        elif jogador == 'pedra' and bot == 'tesoura' or jogador == 'papel' and bot == 'pedra' or jogador == 'tesoura' and bot == 'papel':
            print(f'Jogador venceu! O computador escolheu {bot.upper()} e o jogador escolheu {jogador.upper()}')
        else: 
            print(f'Computador venceu! O computador escolheu {bot.upper()} e o jogador escolheu {jogador.upper()}')
        continuar = input('Deseja continuar jogando? (S/N): ').lower().strip()
        if continuar == 'n':
            break
