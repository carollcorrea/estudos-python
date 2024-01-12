# HIBRIDOS / KEYWORD ONLY ND POSITIONAL ONLY

def criar_carro(modelo, ano, placa ,/, *, marca, motor, combustivel):
       print(modelo, ano, placa, marca, motor, combustivel)

#modelo ano e placa por posição
#marca motor e combustível por nome.

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#válido, pois obedece a regra do modelo ano e placa por posição e marca motor e combustível por nome.

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#inválida pois está nomeando todos e não é o que a função determoina em sua estrutura.

def criar_carro(modelo, ano, placa ,/, marca,*,  motor, combustivel):
       print(modelo, ano, placa, marca, motor, combustivel)
       #Aqui a marca é OPCIONAL devido ao seu posicionamento