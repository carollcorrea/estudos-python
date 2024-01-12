contato = {
    "guilerme@gmail.com": {"nome":"Guilherme", "telefone":"3333-2221"}
}

contato.setdefault("nome", "Giovana")
print(contato)
#Aqui estou supresa, pois não era para acrescentar "Giovana".
# O esperado era que ignorasse essa instrução pois já existe a chave "nome"


contato.setdefault("idade", 28)
print(contato)
# e aqui sai o nome Giovana tb 

#CORREÇÃO:

contato = {
    "guilerme@gmail.com": {"nome":"Guilherme", "telefone":"3333-2221"}
}

contato["guilerme@gmail.com"].setdefault("nome", "Giovana")
print(contato)

contato["guilerme@gmail.com"].setdefault("idade", 28)
print(contato)

#Explicação *Gustavo*: temos um dicionário dentro de um dicionário. Para acessar o segundo dicionário, que é o que eu quero no exemplo, preciso colocar a chave desse segundo dicionário.
#O que está feito no expemplo inicial é acessar somente o primeiro dicionário, onde não tem o nome Giovana, e por isso ele adiciona tranquilamente.
#para acessar um 'subdicionário' preciso estruturar o pedido conforme acima. O .setdefault saberá que terá que 'entrar ' nessa segunda chave para operar.


