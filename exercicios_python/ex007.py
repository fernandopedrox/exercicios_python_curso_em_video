n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
print(f"sua média é {media:.2f}")
if media < 7:
    print(f"Como sua média foi {media:.2f}, infelizmente você está reprovado!")
else:
    print(f"Parabéns! sua média foi de {media:.2f}, você está aprovado!")
