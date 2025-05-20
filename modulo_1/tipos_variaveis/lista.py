# Declaração
minha_lista = [1, 2, 3, 4, 5, "Rocktseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo o indice 0
print("minha_lista[0]:", minha_lista[0])

# Exibindo o indice 5
print('minha_lista[5]:', minha_lista[5])

# Exibindo do indice 1 a 7
print('minha_lista[1:7]:', minha_lista[1:7])

# Exibindo do indice 0 a 6
print('minha_lista[:6]:', minha_lista[:6])

# Exibindo do indice 2 pra frente
print('minha_lista[2:]:', minha_lista[2:])


# Mudando o indice 0
minha_lista[0] = "Python"

# Exibindo o novo indice 0
print('minha_lista[0]:', minha_lista[0])


# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6): ", minha_lista)

# Método index: Ele diz qual é o indice do elemento
indice = minha_lista.index(6)
print('O indice do elemento (6) =', indice)

# Método insert: Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista) 

# Método pop : método de remoção
elemento_removido = minha_lista.pop(3)
print('Elemento removido: ', elemento_removido)
print('Apos o pop(3)', minha_lista)

# Método remove
minha_lista.remove(True)
print('Apos remove(True): ', minha_lista)

#Método sort: organiza a lista em forma crecente. obs só funciona em números
minha_lista_numeros = [10, 3, 5, 4, 9, 7, 60, 45, 9, 2, 1, 7]
minha_lista_numeros.sort()
print('Apos o sort()', minha_lista_numeros)