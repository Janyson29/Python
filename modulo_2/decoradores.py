def meu_decorador(func):
  def wrapper():
    print("antes da função ser chamada")
    func()
    print("depois da função ser chamada")
  return wrapper

@meu_decorador
def minha_funcao():
  print("Minha função foi chamada")

minha_funcao()

class meuDecoradorDeClasse:
  def __init__(self, func):
    self.func = func

  def __call__(self):
    print("Antes da função ser chamada (decoredor de classe)")
    self.func()
    print("Depois da função ser chamada (decoredor de classe)")

@meuDecoradorDeClasse
def segunda_funcao():
  print("A segunda função foi chamada")

segunda_funcao()
