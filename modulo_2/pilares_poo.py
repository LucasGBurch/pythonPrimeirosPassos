# Herança
print("\nExemplo de herança:")

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def andar(self):
    print("O animal {self.nome} andou.")
    return

  def emitir_som(self):
    pass

class Cachorro(Animal): # Herança
  def emitir_som(self):
    return "Latidos"
  
class Gato(Animal): # Herança
  def emitir_som(self):
    return "Miados"


dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

# Polimorfismo
print("\nExemplo de polimorfismo:")
animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} produz: {animal.emitir_som()}")

# Encapsulamento
print("\nExemplo de encapsulamento:")
class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo # __ significa atributo privado! Só quem está DENTRO DESTA CLASSE pode usar
  
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      print(f"R${valor} adicionado à conta.")
    else:
      print("Valor inválido. Deposite valores positivos")

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor
      print(f"R${valor} sacado da conta.")
    else:
      print("Valor inválido. Saque valores positivos, menores ou iguais ao saldo.")

  def consultar_saldo(self):
    return self.__saldo

# Utilizando a classe com valores e métodos encapsulados:
conta = ContaBancaria(1000)
print(f"Saldo da conta bancária: R${conta.consultar_saldo()}.")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: R${conta.consultar_saldo()}.")
conta.depositar(valor=-500)
conta.sacar(valor=1600)
print(f"Saldo da conta bancária: R${conta.consultar_saldo()}.")
conta.sacar(valor=600)
print(f"Saldo da conta bancária: R${conta.consultar_saldo()}.")

conta_do_zezinho = ContaBancaria(saldo=50)

# Abstração:
print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC): # Uma classe abstrata DEFINE métodos, mas NÃO OS IMPLEMENTA!!

  @abstractmethod # Decorator
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo): # PRECISA IMPLEMENTAR OS MÉTODOS DEFINIDOS EM VEÍCULO!!
  def __init__(self) -> None:
    pass
  
  def ligar(self):
      return "Carro ligado usando a chave."
    
  def desligar(self):
      return "Carro desligado usando a chave."

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
