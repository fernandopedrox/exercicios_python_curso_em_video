lista = ()
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$  "))
    lista += ((produto, preco),)
    while True:
        sair = str(input("Deseja sair? [S/N]: ")).strip().lower()
        if sair == "s":
            break
        elif sair == "n":
            print("Escolha defina novos produtos.")
            break
        else:
            print("Digite corretamente! Apenas [S/N]")
    if sair == "s":
        break

print("-" * 20)
print(f"{"Lista de preços":^20}")
print("-" * 20)
for produto, preco in lista:
    print(f'{produto:.<20}R$ {preco:.>.2f}')
