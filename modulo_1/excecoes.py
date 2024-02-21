print("Exemplo de captura de exceções")

try:
  numero = int(input("Digite um número inteiro: "))
  resultado = 10 / numero
except ValueError as e:
  print(f"Erro de value error: {e}") # Ex: a
  raise ValueError("Tipo de variáveis incompatíveis")
except Exception as e:
  print(f"Erro: {e}") # Ex: 0
else: # O else só executa quando não cai nas Exceções
  print(f"Resultado: {resultado}")
finally: # Exceto quando o raise for chamado, o finally sempre executa
  print("Operação finalizada")
