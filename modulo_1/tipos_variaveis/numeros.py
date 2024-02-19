# Números Inteiros
numero_inteiro = 3
print("Inteiro = ", numero_inteiro)

# Real com ponto flutuante (float)
numero_real = 3.14
print("Real com ponto flutuante = ", numero_real)

# função type()
print("Tipo da variável inteiro = ", type(numero_inteiro))
print("Tipo da variável real = ", type(numero_real))

# soma +
soma = numero_real + numero_inteiro
print("Soma dos valores: ", soma)
print("Tipo da soma: ", type(soma))

# subtração -
subtracao = numero_inteiro - numero_real
print("Subtração dos valores: ", subtracao)

# multiplicação *
produto = numero_inteiro * numero_real
print("Multiplicação dos valores: ", produto)

# divisão /
divisao = numero_real / numero_inteiro
print("Divisão dos valores: ", divisao)

# int() para converter em inteiro
print("Valor em inteiro da divisão: ",int(divisao))

# float para converter em real
print("Convertendo inteiro em real: ", float(numero_inteiro))

# resto %, o famoso "módulo"
resto = numero_real % numero_inteiro
print("Resto da divisão: ", resto)

# divisão em inteiro //
divinteiro = numero_real // numero_inteiro
print("Divisão inteira (como se retirasse o módulo do resultado): ", divinteiro)
