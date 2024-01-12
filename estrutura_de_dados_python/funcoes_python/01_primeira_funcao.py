def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")
#Quando eu não passar o argumento da função ao declarar a função, vou precisar passar durante a execução da função.
#Se não passar nenhum valor dá erro.

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")
#Quando eu passo o valor ao declarar a função, a declaração do argumento no momento que estou chamando a função é opcional
#nesse caso, se não for passado o argumento ao chamar a função, o valor será o que foi declarado inicialmente.

exibir_mensagem()
exibir_mensagem_2(nome=" Guilherme ")
exibir_mensagem_3()
exibir_mensagem_3(nome=" Chappie ")   

#Argumentos Nomeados:

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


#FOMAS DE CHAMAR ESSA FUNÇÃO:

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") 

#só passando valores de forma sequencial. Desvantagem: se por alGum motivo o
#Usuário inverter o valor, simplesmente vai acontecer essa troca, e o python não vai saber o que aconteceu.


salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") 
#passando o conjunto chave valor. 
#A vantagem de ter o argumento nomeado é evitar essa troca. Pode acontecer alteração no código durante o fluxo, 
# e sem testes isso vai para a produção.No caso de erro no código, ele executa com erro, precisa ser passado 
# corretamente o argumento EM ORDEM DE DECLARAÇÃO!


salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"}) 
# Os asteriscos indicam que estou passando um dicionário para essa função. 

