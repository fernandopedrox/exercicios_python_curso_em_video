from datetime import date
nascimento = int(input("Digite seu ano de nascimento: "))
data = date.today().year
idade = data - nascimento
if idade <= 9:
    print(f"você tem {idade} anos, está na categoria MIRIM")
elif idade <= 14:
    print(f"você tem {idade} anos, está na categoria INFANTIL")
elif idade <= 19:
    print(f"Você tem {idade} anos, está na categoria JUNIOR")
elif idade == 20:
    print(f"Você tem {idade} anos, está na categoria SÊNIOR")
else:
    print(f"Você tem {idade} anos, está na categoria MASTER")
