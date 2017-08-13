def organiza(lista, inicio):
	for i in range(inicio, len(lista)):
		lista[i] = lista[i]
	return lista
	
def remove_repetidos(lista):
	lista = sorted(lista)
	imprimir(lista)
	newLista = []

	for i in lista:
		if i not in newLista:
			newLista.append(i)
		
	return newLista

def imprimir(lista):
        for i in lista:
                print(i)
	
lista = {1,1,2,3,4,7,10}
remove_repetidos(lista)
print(lista)
