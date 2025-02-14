# Ecercício 1
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Ecercício 2
idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

# Ecercício 3

numero = 7  
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Ecercício 4

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")


# Ecercício 5

numero = int(input("Digite um número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print("O número é múltiplo de 5 e 7.")
else:
    print("O número não é múltiplo de 5 e 7.")

# Ecercício 6

numero = float(input("Digite um número: "))

if numero > 10:
    print("O número é positivo e maior que 10.")
elif numero > 0:
    print("O número é positivo, mas não é maior que 10.")
else:
    print("O número não é positivo.")

# Ecercício 7

numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print("O número é divisível por 3 ou 5.")
else:
    print("O número não é divisível por 3 ou 5.")