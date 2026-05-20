r1 = int(input("Digite o comprimento do primeiro segmento de reta: "))
r2 = int(input("Digite o segundo comprimento de reta: "))
r3 = int(input("Digite o teriro comprimento de reta: "))
if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print("Os segmentos de reta não podem formar um triângulo")
else:
    if r1 == r2 == r3:
        print("Os segmentos formam um triângulo equilátero")
    elif r1 != r2 != r3 != r1:
        print("Os segmentos formam um triângulo escaleno")
    else:
        print("Os segmentos formam um triângulo isósceles")
