def multiplicar_tres_numeros(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
resultado = multiplicar_tres_numeros(num1, num2, num3)
print(f"O resultado da multiplicação é: {resultado}")