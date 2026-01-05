def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha a operação: "))
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == 1:
    print(soma(a, b))
elif op == 2:
    print(subtracao(a, b))
elif op == 3:
    print(multiplicacao(a, b))
elif op == 4:
    print(divisao(a, b))
else:
    print("Opção inválida")
