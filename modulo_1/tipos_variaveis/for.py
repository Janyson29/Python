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