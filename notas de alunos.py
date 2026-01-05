notas = {
    "Ana": 5,
    "João": 9,
    "Maria": 3,
    "Pedro": 7,
    "Lucas": 8.5
}

maior = max(notas, key=notas.get)
media = sum(notas.values()) / len(notas)

print("Maior nota:", maior)
print("Média da turma:", media)
