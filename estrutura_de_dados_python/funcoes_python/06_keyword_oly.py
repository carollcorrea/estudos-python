# KEYWORD ONLY

def criar_carro(*, modelo, ano, placa , marca, motor, combustivel):
       print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#instrução válida, pois todos os argumentos sçao passados de forma nomeada, coforme pede a função.

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#inválido, justamente pq eu estou passando essa necessidade de nomeação para ele através do asterisco.