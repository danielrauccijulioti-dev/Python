maior = int(input("Digite o primeiro número: "))

for i in range(4):
    numero = int(input("Digite outro número: "))
    if numero > maior:
        maior = numero

print("o maior número é:", maior)
