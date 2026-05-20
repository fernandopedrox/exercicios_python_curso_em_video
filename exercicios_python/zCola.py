import math
import random

while True:
    categorias = {
        "1": ("Fatiamento", [
            "frase[:5] -> Do início até o índice 5",
            "frase[11:13] -> Entre o índice 11 e o 13",
            "frase[15:] -> Do índice 15 até o final",
            "frase[9::3] -> Começa no 9, vai até o fim pulando de 3 em 3"
        ]),
        "2": ("Análise", [
            "len(frase) -> Conta o total de caracteres",
            "frase.count('o') -> Conta quantas vezes a letra aparece",
            "frase.find('deo') -> Mostra a posição onde começa o termo",
            "'Curso' in frase -> Verifica se a palavra existe na frase"
        ]),
        "3": ("Transformação", [
            "frase.replace('A', 'B') -> Substitui A por B",
            "frase.upper() / .lower() -> Tudo para MAIÚSCULO ou minúsculo",
            "frase.capitalize() -> Só a 1ª letra da frase em maiúscula",
            "frase.title() -> 1ª letra de cada palavra em maiúscula",
            "frase.strip() -> Remove espaços inúteis no início e fim"
        ]),
        "4": ("Divisão e Junção", [
            "frase.split() -> Divide o texto em uma lista de palavras",
            "'-'.join(frase) -> Junta palavras usando o traço entre elas"
        ])
    }

    print("\n" + "="*40)
    print("--- 📚 BIBLIOTECA DE CONSULTA ---")
    for num, (nome, _) in categorias.items():
        print(f"{num} - ###{nome}###")
    print("5 - Primeira e última palavra")
    print("6 - Funcionalidades: MATH e RANDOM")
    print("7 - O que cada função faz (Dicionário)")
    print("0 - SAIR")
    print("="*40)

    escolha = input("\nEscolha uma opção: ")

    if escolha == "0":
        print("Saindo...")
        break

    elif escolha in categorias:
        nome, comandos = categorias[escolha]
        print(f"\n--- Comandos de {nome} ---")
        for c in comandos:
            print(f"👉 {c}")

    elif escolha == "5":
        print("\n📌 Primeira e última palavra:")
        print("Código:\ndividido = frase.split()\nprint(dividido[0], dividido[-1])")

    elif escolha == "6":
        print("\n📐 MÓDULO MATH:")
        print("  - ceil: Arredonda para cima.")
        print("  - floor: Arredonda para baixo.")
        print("  - trunc: Elimina a parte decimal.")
        print("  - sqrt: Calcula a raiz quadrada.")
        print("  - pow: Faz cálculo de potência.")
        print("\n🎲 MÓDULO RANDOM:")
        print("  - randint: Sorteia um número inteiro.")
        print("  - choice: Escolhe um item aleatório de uma lista.")
        print("  - shuffle: Embaralha uma lista.")
        print("  - random: Gera número flutuante entre 0 e 1.")

    elif escolha == "7":
        print("\n📖 DICIONÁRIO DE FUNÇÕES:")
        print("🔹 len: Conta caracteres/itens.")
        print("🔹 split: Transforma texto em lista.")
        print("🔹 count: Conta repetições de um termo.")
        print("🔹 strip: Remove espaços inúteis.")
        print("🔹 join: Une elementos de uma lista.")

    else:
        print("\nOpção inválida!")

    input("\nPressione Enter para continuar...")
