compras = []

while True:
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Ver lista")
    print("4 - Limpar")
    print("5 - Sair")
    op = input("Escolha: ")

    if op == "1":
        compras.append(input("Item: "))
    elif op == "2":
        compras.remove(input("Item: "))
    elif op == "3":
        print(compras)
    elif op == "4":
        compras.clear()
    elif op == "5":
        break
