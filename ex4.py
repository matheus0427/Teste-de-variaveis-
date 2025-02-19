def mensagem_idade(idade):
    # Verifica se a idade digitada é 18
    if idade == 18:
        print("Parabéns! Você acabou de atingir a maioridade.")
    else:
        print("Obrigado por informar sua idade!")

# Exemplo de uso
idade = int(input("Digite sua idade: "))

# Chamando a função
mensagem_idade(idade)