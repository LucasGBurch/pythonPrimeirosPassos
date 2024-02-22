# @classmethod
# @staticmethod

class MinhaClasse:
  valor = 10 # Atributo da classe
  def __init__(self, nome) -> None:
    self.nome = nome # Atributo da instância
  
  # requer uma instância para ser chamado
  def metodo_instancia(self): # self é referência da instância
    return f"Método de instância chamado para {self.nome} e valor {self.valor}"
  
  @classmethod
  def metodo_classe(cls):
    return f"Método de classe chamado para valor={cls.valor}" # Aqui o "nome" não é acessível

  @staticmethod
  def metodo_estatico(): # Estático não recebe a referência da classe (cls)
    return "Método estático chamado"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
# print(MinhaClasse.metodo_instancia()) # NÃO FUNCIONA CHAMAR DIRETAMENTE DA CLASSE SEM INSTANCIAR EM UM OBJETO
print(MinhaClasse.valor) # ESTE FUNCIONA POIS O ATRIBUTO É DA CLASSE

# Conseguimos chamar métodos se usarmos o decorator classmethod
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",")
    return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

  @staticmethod # ATENÇÃO! Muitos métodos estáticos dispensa criação de instância, o que não é bom
  def somar(a, b): # Melhor pensar além dos comportamentos dos métodos, criando métodos de instância!
    return a + b # Senão, o código tende a ficar bagunçado.
  
print(f"A soma na classe matemática é: {Matematica.somar(a=10, b=15)}")
