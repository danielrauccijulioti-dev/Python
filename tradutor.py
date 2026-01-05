tradutor = {
    "construção": "building",
    "cadeira": "chair",
    "aviso": "warning",
    "perigoso": "danger",
    "chave": "key",
    "horas": "hours",
    "semanas": "weeks",
    "vida": "life",
    "tradutor": "translate",
    "por favor": "please"
}

palavra = input("Digite uma palavra: ")
print(tradutor.get(palavra, "Palavra não encontrada"))
