print('For utilizando uma lista')
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print('For utilizando uma tupla')
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "Pedro", "idade": 29, "cidade": "Brasilia"}
print("For utilizando dicionário - chave")
for chave in pessoa.keys():
  print(chave)

print("\n For utilizando dicionário - valores")
for valor in pessoa.values():
  print(valor)

print("\n For utilizando dicionário - itens")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

#Range(): retorna um intervalo númerico
#[0,1,2,3,4,5,6,7,8,9]
print('\n Utilizando a função range()')
for numero in range(5):
  print('Número:', numero)

print('\n Utilizando a função range()')
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
  print("Indice:", indice)
  print("Elemento:", lista[indice])
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")