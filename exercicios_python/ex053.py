nome = input("Digite uma frase para verificar se é um palíndromo: ").strip().lower().split()
nome = "".join(nome)
palindromo = ""
for c in nome[::-1]:
    palindromo += c
if nome == palindromo:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
