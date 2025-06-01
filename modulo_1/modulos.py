print("Exemplo de importação de módulo padrão:")
# import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")

# import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = saudacao("Pedro")
resultado_dobro = dobro(5)
print(mensagem)
print(resultado_dobro)