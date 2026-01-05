agenda = {}

while True:
    print("1 - Adicionar")
    print("2 - Buscar")
    print("3 - Listar")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        tel = input("Telefone: ")
        agenda[nome] = tel
    elif op == "2":
        nome = input("Nome: ")
        print(agenda.get(nome, "Contato não encontrado"))
    elif op == "3":
        print(agenda)
    elif op == "4":
        break
