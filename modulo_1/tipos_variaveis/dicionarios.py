# Criando um dicionário de exemplo
pessoa = {"nome": "Lucas", "idade": 33, "cidade": "Porto Alegre"} # Uma chave seguida de um valor

# Acrescentando chave-valor novo:
pessoa["sobrenome"] = "Burch"
print("Sobrenome:", pessoa["sobrenome"])

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Alterar valor existente
pessoa["idade"] = 34
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
# keys
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0]) # Repara como foi necessário converter as chaves obtidas no keys() em uma lista

# values
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Segundo valor do dicionário:", valores[1])

# items: cada elemento é uma tupla com seus valores (chave, valor)
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro chave-valor: %s = %s" % (itens[0][0], itens[0][1])) # 0 é o primeiro par, 1 é o segundo item dentro do par, que é o valor nome
