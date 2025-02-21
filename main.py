import random
def gerar_numero_aleatorio_5_10():
    return random.randint(5, 10)
def gerar_tres_numeros_aleatorios():
    return [random.randint(1, 100) for _ in range(3)]
def gerar_numero_aleatorio_10_30():
    return random.choice(range(10, 31))
def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")
def soma_numeros_pares():
    numero = int(input("Digite um número inteiro positivo: "))
    soma = 0
    for i in range(2, numero + 1, 2):
        soma += i
    print(f"A soma dos números pares de 2 até {numero} é: {soma}")
def tabuada_multiplicacao():
    numero = int(input("Digite um número inteiro: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
def numeros_impares_reversos():
    for i in range(99, 0, -2):
        print(i)
def main():
    print("=== Módulo 1: Número aleatório entre 5 e 10 ===")
    print("Número gerado:", gerar_numero_aleatorio_5_10())
    print()
    print("=== Módulo 2: Gerar 3 números aleatórios ===")
    print("Números gerados:", gerar_tres_numeros_aleatorios())
    print()
    print("=== Módulo 3: Número aleatório entre 10 e 30 ===")
    print("Número gerado:", gerar_numero_aleatorio_10_30())
    print()
    print("=== Módulo 4: Contagem regressiva ===")
    contagem_regressiva()
    print()
    print("=== Módulo 5: Soma de números pares ===")
    soma_numeros_pares()
    print()
    print("=== Módulo 6: Tabuada de multiplicação ===")
    tabuada_multiplicacao()
    print()
    print("=== Módulo 7: Números ímpares reversos ===")
    numeros_impares_reversos()
    print()
if __name__ == "__main__":
    main()