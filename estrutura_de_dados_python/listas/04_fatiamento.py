lista=["p","y","t","h","o","n"]

print(lista[2:]) #índice inicial 2, será a letra t. índice final não passado, irá até o final. 
#resposta esperada:  ["t","h","o","n"] pois o ínice inicial é inlcusivo.
print(lista[:2]) #índice inicial não passado, será o primeiro elemento da lista. índice final 2, será a letra y. 
#resposta esperada ["p","y"], pois o índice final é exclusivo.
print(lista[1:3]) #indice inicial 1, será y. indice final 3. será y.
#resposta esperada ["y", "t"] pois o índice final é exclusivo.
print(lista[0:3:2]) #indice inicial 0,final 3, ínice final 2.
#resposta esperada ["p","t"]
print(lista[::]) #índice vazio, considera todos os elementos.
#resposta esperada ["p","y","t","h","o","n"]
print(lista[::-1]) #nesse formato revertemos a ordem da lista. lista reversa.
#resposta esperada ["n", "o", "h", "t","y","p"]


