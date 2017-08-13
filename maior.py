def maior_elemento (lista):
    maior = lista[0]

    for i in lista:
        if i > maior:
            maior = i
    return maior

lista = [1,2,3,4,5,6]
print(maior_elemento(lista))
