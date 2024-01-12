numeros=[1,30,21,2,9,65,34]
pares=[]

#filtroV1

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# com compreensão, isso fica assim:

numeros=[1,30,21,2,9,65,34]
pares=[numero for numero in numeros if numero % 2==0]

print(pares)

#Modificando valores, v1:

numeros=[1,30,21,2,9,65,34]
quadrado=[]

for numero in numeros: #para cada número em números
    quadrado.append(numero**2) #eleve o valor ao quadrado

# com compreensão, isso fica assim:

numeros=[1,30,21,2,9,65,34]
quadrado=[numero**2 for numero in numeros] #eleve ao quadrado cada número em números.

        