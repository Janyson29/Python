# Exemplo
def saudacao(nome):
  print(f'Olá, {nome}!')

print("\nChamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

# função com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(5)
print('Resultado da função quadrado:', resultado_quadrado)

#função com multiplos parametros
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print("\nChamando a função soma:")
numero1 = 25
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do número %s e número %s é: %s" % (numero1, numero2, resultado_soma))