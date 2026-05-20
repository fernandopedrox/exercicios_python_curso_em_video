velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print(f"""você foi multado por excesso de velocidade! Velocidade: {velocidade} km/h
Sua multa é de R$ {(velocidade - 80) * 7}""")
