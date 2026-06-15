contador = 0
n = int(input("Digite o primeiro número: "))
r = int(input("Digite a razão: "))
termos = int(input("Digite quantos termos você quer mostrar: "))
continuar = 0
while termos != 0:
    continuar += termos
    while contador < continuar:
        print(n, end=" ")
        n += r
        contador += 1
    print("pausa")
    termos = int(input("Deseja adicionar mais quantos termos?: "))
print(f"Progressão finalizada com {contador} termos mostrados.")
