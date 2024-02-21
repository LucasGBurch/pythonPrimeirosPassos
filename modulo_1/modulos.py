print("Exemplo de importação de módulo padrão:")
# import math
from math import sqrt

valor = 144
raiz_quadrada = sqrt(valor) # em vez de math.sqrt(valor), para não importar TUDO
print(f"A raiz quadrada de {valor} é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")
# import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = saudacao("Lusca")
numero = 31
resultado_dobro = dobro(numero)
print(mensagem)
print(f"O dobro de {numero} é {resultado_dobro}.")
