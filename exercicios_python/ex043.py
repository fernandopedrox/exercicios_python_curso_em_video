peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f"Seu IMC é de {imc:.1}, você está abaixo do peso.")
elif imc <= 25:
    print(f'Seu IMC é de {imc:.1f}, você está no peso ideal')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.1f}, você está com sobrepeso')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.1f}, você está com obesidade')
else:
    print(f'Seu IMC é de {imc:.1f}, você está com obesidade mórbida')
