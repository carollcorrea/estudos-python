linguagens=["python","js","c","java","csharp"]

print(sorted(linguagens, key=lambda x:len(x))) #argumento é o tamanho da palavra.

print(sorted(linguagens, key=lambda x:len(x), reverse=True)) #argumento é o tamanho reverso da palavra.