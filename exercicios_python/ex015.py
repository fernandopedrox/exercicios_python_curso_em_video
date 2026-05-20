valor_multa = 20
multa = 0
km_rodado = float(input("Quantos quilometros foram rodados?: "))
dias_alugados = int(input("Quantos dias foram alugados?: "))
devolucao_dias = int(input("Em quantos dias o corro foi devolvido?: "))
if devolucao_dias > dias_alugados:
    multa = (devolucao_dias - dias_alugados) * valor_multa
    preco = multa + 60 * dias_alugados + 0.15 * km_rodado
    print(f"O preço a se pagar é de R$ {preco:.2f} *preço foi acrescido de multa por atraso*")
else:
    preco = 60 * dias_alugados + 0.15 * km_rodado
    print(f"O preço a se pagar é de R$ {preco:.2f}")
