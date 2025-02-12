# Solicita ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realiza as operações
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Verifica se o segundo número é zero para evitar divisão por zero
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Erro: divisão por zero não é permitida."

# Exibe os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)