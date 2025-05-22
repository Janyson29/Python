#Criando um dicionário de exemplo
pessoa = {"nome": "Pedro", "idade": 30, "cidade": "Rio de Janeiro"}

#Exibindo o dicionário
print("Meu dicionário de exemplo: ", pessoa)

#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

#Adicionando uma chave
pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionário de exemplo: ", pessoa)

#Atualizando uma chave
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

#Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo: ", pessoa)

#Métodos: keys(), values(), items()
#Keys()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

#Values()
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

#Items()
itens = list(pessoa.items())
print("Pares chave-valor do dicionário: ", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))