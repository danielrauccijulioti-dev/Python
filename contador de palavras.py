frase = input("Digite uma frase: ").lower()
palavras = frase.split()
contador = {}

for p in palavras:
    contador[p] = contador.get(p, 0) + 1

print(contador)
