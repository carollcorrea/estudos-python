def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor
#esse return vem em uma tupla (faz sentido pq é um valor imutável)


def func_3():
    print("Olá mundo!")
    #return None (por padrão esse é o comportamento)


print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())
#essa ultima retorna None pois não foi passado parâmetro