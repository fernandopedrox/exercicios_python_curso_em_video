total_gasto = produtos_mais_1000 = barato = 0
produto_barato = ""
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    total_gasto += preco
    if preco >= 1000:
        produtos_mais_1000 += 1
    if barato == 0:
        barato = preco
        produto_barato = nome
    else:
        if barato > preco:
            barato = preco
            produto_barato = nome
    continuar = ""
    while continuar not in "sn":
        continuar = input("Deseja continuar?[S/N]: ").strip().lower()
    if continuar == "n":
        break
print(f"""O produto mais barato foi o/a {produto_barato} custando {barato} reais
o total de produtos custando mais de 1000 reais foi {produtos_mais_1000}""")
