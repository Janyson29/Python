print("Exemplo de captura de excecões")
try:
  numero = int(input("Digite um número inteiro: "))
  resultado = 10 / numero
  print(f"O resultado é: {resultado}")
except ValueError as e:
  print(f"Erro de value error: {e}")
  raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
  print(f"Erro: {e}")
else:
  print(f"Resultado: {resultado}")
finally:
  print("Operção finalizada")