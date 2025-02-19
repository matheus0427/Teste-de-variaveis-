from datetime import datetime
def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    if ano_nascimento > ano_atual or ano_nascimento < 1900:
        return "Ano de nascimento inválido."
    idade = ano_atual - ano_nascimento
    return idade
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = calcular_idade(ano_nascimento)

if isinstance(idade, int):
    print(f"Você tem {idade} anos.")
else:
    print(idade)