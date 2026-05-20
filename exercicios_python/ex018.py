from math import degrees, radians, cos, sin, tan
angulo = int(input("Digite um ângulo: "))
graus = radians(angulo)
cosseno = cos(graus)
seno = sin(graus)
tangente = tan(graus)
print(f"O cosseno de {angulo:.0f} é {cosseno:.2f}, seu seno é {seno:.2f} e sua tangente é {tangente:.2f}")
