pessoa = {
    "nome": "daniel",
    "idade": 16,
    "cidade": "São Paulo"
}

chave = input("O que deseja consultar? ")
print(pessoa.get(chave, "Informação não encontrada"))
