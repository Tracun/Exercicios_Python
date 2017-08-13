def inverte(lista):
    x = len(lista)-1
    print(x)
    newLista = lista
    
    for i in lista:
        print(i)
        
        newLista[x] = i
        x -= 1
        
    return newLista







lista = [1,2,3,4,5,6]
print(inverte(lista))
