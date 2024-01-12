# POSITIONAL ONLY


def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
       print(modelo, ano, placa, marca, motor, combustivel)

       #modelo ano e placa eu sou obrigado a passar sem o parâmetro nomeado, somente por posição.
       #marca motor e combustível possp passar nomeado.


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #instrução válida

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 
#Instrução inválida, pois passei modelo, ano e placa nomeados e pela localização, são argumentos posicionais e não podem ser nomeados.
#TypeError: criar_carro() got some positional-only arguments passed as keyword arguments: 'modelo, ano, placa'