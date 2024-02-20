# Declaração

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Meu exemplo de lista", minha_lista)

# Exibindo elementos da lista separados ou em intervalos
minha_lista[0] = "python" # Atribuindo novo elemento à posição da lista
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7]) # do minha_lista[1] ao minha_lista[6]
print(minha_lista[:6]) # [0:6]
print(minha_lista[2:]) # [2:8] do [2] ao último

# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Índice do elemento 6:", indice)

# Método insert: Insere um elemento em um índice específico
minha_lista.insert(2, 10) # O que estava em [2] é jogado para frente na lista
print("Após o insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3) # Os outros elementos recuam na lista a partir da posição do item removido
print("Elemento removido: ", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove
minha_lista.remove(True) # Remove o primeiro True encontrado
print("Após o remove(True):", minha_lista)

lista_numerica = [1, 20, 0, 2, 5, 4, 7]
# Método sort
lista_numerica.sort() # Buga numa lista com tipos diferentes;
print("Após sort():", lista_numerica) # Só funciona numa lista com elementos do mesmo tipo (ex: int)
