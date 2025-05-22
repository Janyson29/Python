# IF, ELIF E ELSE

#Exemplo de 'if'
idade = int(input("Quantos anos você tem?"))
print("Exemplo de comando if")
#Maior ou igual a:
if idade >= 18:
  print('Você é maior de idade.')

#Igual a:
if idade == 19:
  print("Você tem 19 anos.")

#Menor ou igual a:
if idade <= 17:
  print("Você é menor de idade.")

#Diferende de:
if idade != 10:
  print("Você não tem 10 anos.")

#elif
if idade <= 17:
  print('Você é menos de idade.')
elif idade >=12:
  print("Você é um adolecente.")
else:
  print("Você é maior de idade.")

#else
if idade <= 17:
  print('Você é menos de idade.')
else:
  print("Você é maior de idade.")


#Exemplo 2
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)