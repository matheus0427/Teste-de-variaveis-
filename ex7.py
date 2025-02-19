def exibir_menu():
    print("\n--- Menu do Restaurante ---")
    print("1. Salada - R$ 10,00")
    print("2. Macarronada - R$ 20,00")
    print("3. Sanduíche - R$ 15,00")
    print("4. Sorvete - R$ 8,00")
    print("5. Sair")
def processar_pedido(opcao):
    if opcao == 1:
        return "Salada", 10.00
    elif opcao == 2:
        return "Macarronada", 20.00
    elif opcao == 3:
        return "Sanduíche", 15.00
    elif opcao == 4:
        return "Sorvete", 8.00
    else:
        return None, 0.00
def main():
    total = 0.00
    pedidos = []
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            if opcao == 5:
                break
            elif 1 <= opcao <= 4:
                item, preco = processar_pedido(opcao)
                pedidos.append((item, preco))
                total += preco
                print(f"\n{item} adicionado ao pedido. Total parcial: R$ {total:.2f}")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 5.")
    if pedidos:
        print("\n--- Resumo do Pedido ---")
        for item, preco in pedidos:
            print(f"{item}: R$ {preco:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
    else:
        print("\nNenhum pedido foi realizado.")

    print("\nObrigado por escolher nosso restaurante!")
if __name__ == "__main__":
    main()