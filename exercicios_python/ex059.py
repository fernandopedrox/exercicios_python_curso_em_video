sair = "continuar"
while sair == "continuar":
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    opcao = int(input("""Digite:
O número [1] para somar
O número [2] para multiplicar
O número [3] para maior
O número [4] para novos números
O número [5] para sair
: """))
    match opcao:
        case 1:
            soma = n1 + n2
            print(f"A soma de {n1:.2f} + {n2:.2f} é igual a {soma:.2f}")
        case 2:
            multiplicar = n1 * n2
            print(f"A multiplicaçao de {n1:.0f} x {n2:.0f} é igual a {multiplicar:.0f}")
        case 3:
            maior = max(n1, n2) 
            menor = min(n1, n2)
            print(f"O maior número é {maior:.2f} e o menor número é {menor:.2f}")
        case 4:
            print('ok')
        case 5: 
            sair = "sair"
            print("Programa encerrado.")
 