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
print("Nome completo (8a forma): %s %s" % (nome, sobrenome)) # Transformacao em string, forma considerada a mais segura
print(f"Nome completo (9a forma): {nome} {sobrenome}") # Forma mais visivel para variaveis
print("Nome completo (10a forma): {} {}".format(sobrenome, nome))
