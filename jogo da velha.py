tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar(r):
    for fileira in r:
        print(" | ".join(fileira))
        print("-" * 9)

mostrar(tabuleiro)
