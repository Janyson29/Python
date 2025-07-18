# POO

# Classe exemplo
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def saudacao(self):
    return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos"

# Objetos
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome='Rodrigo', idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)

pessoa3 = Pessoa('Pedro', 26)
mensagem = pessoa3.saudacao()
print(mensagem)