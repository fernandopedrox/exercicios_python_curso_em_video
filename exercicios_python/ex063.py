c = 0
t1 = 0
t2 = 1
termos = int(input("Digite quantos termos da sequência de Fibonacci você deseja: "))
if termos == 0:
    print("Nenhum termo da sequência de Fibonacci será exibido.")
elif termos == 1:
    print(t1)
elif termos == 2:
    print(t1, t2)
else:
    print(t1, t2, end=" ")
    while c < termos - 2:
        t3 = t1 + t2
        print(t3, end=" ")
        t1 = t2
        t2 = t3
        c += 1
        