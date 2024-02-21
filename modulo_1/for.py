lista = [1, 2, 3, 4, 5]

print("For utilizando lista:")
for elemento in lista:
  print(elemento)

print("For utilizando tupla:")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "Lucas", "idade": 33, "cidade": "Porto Alegre"}
print("For utilizando dicionário - chaves")
for chave in pessoa.keys():
  print(chave)

print("\nFor utilizando dicionário - valores")
for valor in pessoa.values():
  print(valor)

print("\nFor utilizando dicionário - chaves: valores")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")


# range(): intervalo numérico
# [0, 1, 2, 3...]
print("\nUtilizando a função range()")
for numero in range(5):
  print("Número:", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
  # print("Índice:", indice)
  # print("Elemento:", lista[indice])

  if indice == 3:
    lista[indice] = 5

print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  if indice == 1:
    print("Índice", indice)
