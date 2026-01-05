matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = sum(sum(linha) for linha in matriz)
diagonal = matriz[0][0] + matriz[1][1] + matriz[2][2]

print("Soma total:", soma_total)
print("Diagonal principal:", diagonal)
