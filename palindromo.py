palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
