# POO

# Classe exemplo
class Pessoa:
  def __init__(self, nome, idade) -> None:
    self.nome = nome
    self.idade = idade
  
  def saudacao(self): # self é uma "referência a si próprio", para acessar atributos da classe
    return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos (instância de uma classe)
pessoa1 = Pessoa(nome="Alice", idade=30)

# print(f"Nome: {pessoa1.nome}")
# print(f"Idade: {pessoa1.idade}")

mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)
