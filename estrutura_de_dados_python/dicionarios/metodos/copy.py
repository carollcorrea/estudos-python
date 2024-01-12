contatos = {
    "guilerme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

copia = contatos.copy()
#Está feita a cópia. Agora vou entrar no dicionário e alterar o valor da chave.
copia["guilerme@gmail.com"] = {"nome":"Gui"}

contatos["guilerme@gmail.com"]
print(contatos)

copia["guilerme@gmail.com"]
print(copia)
