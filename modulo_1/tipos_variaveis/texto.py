# Declaração

nome_completo = "Lucas Burch"

nome_completo_aspas = """Lucas
Burch"""

nome_completo_quebra = "Lucas \
Burch" # Igual ao nome completo. Só declarada diferente

nome = "Lucas"
sobrenome = "Burch"

#Formatação
print("Nome completo (1a forma):", nome_completo) # Concatenação com esta vírgula gera um espaço automático
print("Nome completo (2a forma): " + nome_completo) # A 2a e a 3a precisa criar o espaço, mesmo que fosse + " " +
print("Nome completo (3a forma): " + "Lucas " + "Burch")
print("Nome completo (4a forma): " + "Lucas", "Burch")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome)) # Transformacão em string, forma considerada a mais segura
print(f"Nome completo (9a forma): {nome} {sobrenome}") # Forma mais visível para variáveis
print("Nome completo (10a forma): {} {}".format(sobrenome, nome))


# MÉTODOS DE TEXTO:
nome.lower() # Minúsculas
nome.upper() # Maiúsculas
nome.count("a") # Contar caracteres
nome.find("a") # Retorna posição da letra
nome.encode() # Converte string em bytes
nome.encode().decode() # Decodifica de volta para tipo texto

nome.replace("a", "b") # Substitui todas as letras a pela b. Exemplo:
telefone = "(19)97325-0502"
telefone.replace("(", "").replace(")", "").replace("-", "")
# Tratamento de dados retirando os parênteses e o traço

"-".join("String") # Coloca traço no meio dos caracteres
nome_completo.split(" ") # Com base no espaço, separa as strings e retorna uma lista com elas

nomeX = "xLucas Burchx"
nomeX.strip("x") # Remove caractere desejado quando ele está no início ou no fim
nomeX.rstrip("x") # Só remove o da direita/último x
nomeX.lstrip("x") # Remove o primeiro, da esquerda

nome_completo.startswith("Lu") # Retorna booleano para string que começa com esses caracteres
