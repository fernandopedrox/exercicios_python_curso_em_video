contador = mais_18 = homens = mulheres_mais_20 = 0
while True:
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().lower()
    if sexo not in "mf":
        print("Sexo inválido. Digite M para masculino ou F para feminino.")
    else:
        idade = int(input("Digite sua idade: "))
        if idade > 18:
            mais_18 += 1
        if sexo == "m":
            homens += 1
        if sexo == "f" and idade > 20:
            mulheres_mais_20 += 1
        contador += 1
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().lower()
        continuar = ""
        while continuar not in "sn":
            continuar = input("Deseja continuar? [S/N]: ")
        if continuar == "n":
            break
        else:
            print("-" * 40)    
print(f"""O total de pessoas cadastradas foi de {contador} pessoas. 
Tendo {mais_18} pessoas com mais de 18 anos.
Sendo {mulheres_mais_20} mulheres com mais de 20 anos.
E com um total de {homens} homens cadastrados""")         
