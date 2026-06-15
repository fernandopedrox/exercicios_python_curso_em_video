fatorial = 1
n = int(input("Digite um número para saber o fatorial: "))
while n > 0:
    fatorial *= n
    print(n, end=" ")
    n = n - 1
print("=", fatorial)
