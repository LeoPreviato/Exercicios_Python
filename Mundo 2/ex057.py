from time import sleep  # Importa a função sleep para pausar o programa por alguns segundos

# Exibe um título centralizado com 50 caracteres preenchidos com "="
print(" Validação de Dados ".center(50, "="))

# Solicita o sexo do usuário
# strip() remove espaços extras
# upper() transforma a letra em maiúscula
sexo = str(input("Digite o seu sexo [M/F]: ")).strip().upper()

# Pausa de 0.8 segundos para melhorar a experiência visual
sleep(0.8)

# Linha em branco para organização
print()

# Mensagem de análise
print("Analisando o seu sexo...")

# Pausa de 1 segundo simulando processamento
sleep(1)

# Verifica se o valor digitado NÃO é "M" e NÃO é "F"
if sexo != "M" and sexo != "F":
    # Enquanto o sexo continuar inválido, o loop se repete
    while sexo != "M" and sexo != "F":
        # Pede novamente o sexo até o usuário digitar corretamente
        sexo = str(input("Sexo incorreto🚫. Digite novamente o seu sexo [M/F]: ")).upper()

# Linha em branco para separar visualmente a saída
print()

# Se o sexo for "M", imprime masculino
if sexo == "M":
    print("Sexo Masculino registrado com sucesso! 🚹")
# Caso contrário, só pode ser "F"
else:
    print("Sexo Feminino registrado com sucesso! 🚺")
