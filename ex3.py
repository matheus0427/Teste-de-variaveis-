def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
resultado = calcular_potencia(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é: {resultado}")