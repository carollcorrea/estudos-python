def exibir_poema(data_extenso, *args, **kwargs): #aqui pode ser qualquer valor ex: *lista **dicionário. Importa os asteriscos.
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Domingo, 01 de outubro de 2023", #primeiro argumento {data_extenso}
    "Zen of Python", #Segundo argumento {texto}
    "beautiful is better than ugly.",#Segundo argumento {texto}
    autor="Tim Peters", 
    ano=1999
)

#Como o python sabe que acaba o args e tem que começar com kwargs: 

#kwargs é uma estrutura de chave=valor. Então quando acabar valores seguindos por virgula e começar 
# o mapeamento de chave=valor ele vai entender que mudou de args para kwargs.