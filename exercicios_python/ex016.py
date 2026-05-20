from math import trunc
n = float(input('Digite um número: '))
print(f'O número {n} inteiro é {trunc(n)}')
#O código pode utilizar o trunc assim como também pode utilizar a formatação de string 
#para mostrar apenas a parte inteira do número, como no exemplo abaixo:

numero = float(input("Digite um número: "))
print(f"sua porção inteira é {numero:.0f}")

