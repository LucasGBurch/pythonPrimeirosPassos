class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando."
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando."
  
class Morcego(Mamifero, Ave): # Herança MÚLTIPLA
  def emitir_som(self):
    # super().emitir_som() # super() chama implementação da classe mãe. Caso essa já tenha algo implementado antes
    return "Morcegos emitem sons ultrassônicos."

morcego = Morcego(nome="Batmé")

# Acessando métodos da classe base "Animal"
print(f"Nome do morcego: {morcego.nome}.")
print("Som do morcego:", morcego.emitir_som())

# Acessando métodos das classes "Mamífero" e "Ave"
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())
