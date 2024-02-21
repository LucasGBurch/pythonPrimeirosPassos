# Exemplo

def saudacao(nome):
  print(f"Olar, {nome}!")

print("\nChamando a função saudacao:")
saudacao("Grupto") # Chamada da função com seu argumento
saudacao("Luskan")

# Função com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\nChamando função quadrado:")

print(f"Resultado da função quadrado: {quadrado(7)}")
print("Resultado da função quadrado:", quadrado(4))

# Função com múltiplos parâmetros
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

primeiro_numero = 21
segundo_numero = 53
resultado_soma = soma(primeiro_numero, segundo_numero)
print("\nChamando a função soma:")
print(f"A soma entre os números {primeiro_numero} e {segundo_numero} é: %s" %
      (resultado_soma))
