# @classmethod
# @staticmethod

class MinhaClasse:
  valor = 10 # Atributo de classe

  def __init__(self, nome):
    self.nome = nome #Atributo da instância

  # requer uma instância para ser chamado
  def metodo_instancia(self):
    return f"Método de instância chamado para {self.nome}"
  
  @classmethod
  def metodo_classe(cls):
    return f"Método de classe chamado para valor={cls.valor}"

obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())