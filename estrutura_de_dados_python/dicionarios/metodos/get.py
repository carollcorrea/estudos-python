contatos = {"guilerme@gmail.com":{"nome":"Guilerme", "telefone":"3333-2221"}}

#contatos["chave"] *Se eu pedir para ele acessar uma chave inesistente dá KeyError. Esse erro pára o programa.

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
#Se ele não encontrar chave, se ele não encontrar retorna um dicionário vazio.
print(resultado)

resultado = contatos.get(
    "guilerme@gmail.com", {}
)
print(resultado)