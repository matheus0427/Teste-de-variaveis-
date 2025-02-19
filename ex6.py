def verificar_copa_mundo(ano):
    # Dicionário com os anos em que o Brasil ganhou a Copa do Mundo
    copas_ganhas_pelo_brasil = {1958, 1962, 1970, 1994, 2002}
    
    # Verifica se o ano está na lista de Copas ganhas pelo Brasil
    if ano in copas_ganhas_pelo_brasil:
        return f"Sim! O Brasil ganhou a Copa do Mundo de {ano}."
    else:
        return f"Não. O Brasil não ganhou a Copa do Mundo de {ano}."

# Exemplo de uso
ano = int(input("Digite o ano da Copa do Mundo: "))

# Chamando a função e exibindo o resultado
resultado = verificar_copa_mundo(ano)
print(resultado)