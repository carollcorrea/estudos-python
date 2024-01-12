pessoa = {"nome": "Guilerme", "idade":"28"}

pessoa = dict(nome="Guilerme", idade="28")
              
#Quando já tenho um dicionário criado e quero adicionar uma info:
pessoa["telefone"] = "3333-1234"
print(pessoa)

#O dicionário não permite que você repita chaves:

pessoa["nome"] = "Maria"
print(pessoa)

#Ele simplesmente substitui um dado pelo outro...