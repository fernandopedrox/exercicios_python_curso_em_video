sexo = ""
while sexo != "m" and sexo != "f":
    sexo = input("Digite seu sexo (M/F): ").lower().strip()
    if sexo != "m" and sexo != "f":
        print("Sexo inválido! Digite (M/F) para definir seu sexo")
print(f"Seu sexo {sexo} foi registrado!")