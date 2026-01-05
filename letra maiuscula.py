frase = input("Digite uma frase: ")
palavras = frase.split()
resultado = " ".join(p.capitalize() for p in palavras)

print(resultado)
