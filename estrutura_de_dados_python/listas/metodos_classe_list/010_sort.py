linguagens=[]

linguagens.append("python")
linguagens.append("js")
linguagens.append("java")
linguagens.append("csharp")

linguagens.sort() #argumento padrão ordem alfabética.
linguagens.sort(reverse=True) #espelha a ordenação de trás para frente
linguagens.sort(key=lambda x:len((x))) #ordem crescente de quantidade de caracteres(menor palavra para a maior palavra).
linguagens.sort(key=lambda x:len((x)), reverse=True) #ordem decrescente de quantidade de caracteres (maior palavra para a menor palavra).





print(linguagens)
