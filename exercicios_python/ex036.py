casa_valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos_pagamento = int(input("Digite em quantos anos para a quitação: "))
prestacao_mensal = casa_valor / (anos_pagamento * 12)
if prestacao_mensal > salario * 30 / 100:
    print("Empréstimo negado!")
else:
    print(f"Empréstimo aprovado! Com prestações mensais de R$ {prestacao_mensal:.2f}")
