from datetime import date
data_atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = data_atual - nascimento
if idade < 18:
    falta = 18 - idade
    print(f"Você tem {idade} anos e ainda não precisa de alistar, ainda falta(m) {falta} ano(s) para o alistamento.")
elif idade == 18:
    print(f"Está na hora de se alistar, você tem {idade} anos e precisará comparecer a um juntar militar")
else:
    passou = idade - 18
    print(f"Você tem {idade} anos e já passou {passou} anos do tempo de se alistar, procure um junta militar para regularizar sua situação")
