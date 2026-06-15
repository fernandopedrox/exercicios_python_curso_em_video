palavras = ()
while True:
    palavras += (input("Digite uma palavra: "),)
    while True:
        sair = input("Deseja sair?[S/N]: ").strip().lower()
        if sair in "sn":
            break
        else:
            print("Digite corretamente!")
    if sair == "s":
        break
for p in palavras:
    print(f"\nA palavra {p} possui as seguintes vogais: ", end = " ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"{letra}", end = " ")
