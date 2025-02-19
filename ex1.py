def comparar_par_impar(num1, num2):
    resultado_num1 = "par" if num1 % 2 == 0 else "ímpar"
    resultado_num2 = "par" if num2 % 2 == 0 else "ímpar"
    return f"O número {num1} é {resultado_num1} e o número {num2} é {resultado_num2}."
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(comparar_par_impar(num1, num2))