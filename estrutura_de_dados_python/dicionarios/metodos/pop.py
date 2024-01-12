contatos = {
    "guilerme@gmail.com": {"nome":"Guilherme", "telefone":"3333-2221"}
}

resultado = contatos.pop("guilerme@gmail.com")
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "nao encontrou")
print(resultado)