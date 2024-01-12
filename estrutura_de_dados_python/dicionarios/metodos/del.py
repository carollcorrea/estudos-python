contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com": {"nome": "Chaipe", "telefone":"3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone":"3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"] #Aqui removi somente o telefone.
del contatos["chappie@gmail.com"] #essa chave não existirá mais no dicionário.

print(contatos)