# Importa a função sleep do módulo time
from time import sleep

# Exibe um título centralizado com 45 caracteres preenchidos por "="
print(" Contagem Regressiva ".center(45, "="))

# Mensagem inicial avisando o início da contagem
print("Começando contagem regressiva para o Ano Novo!")

# Pausa de 1 segundo antes de iniciar a contagem
sleep(1)

# Laço for que realiza a contagem regressiva
# range(10, 0, -1) significa:
# começa em 10, termina em 1 e decrementa de 1 em 1
for cont in range(10, 0, -1):
    # Exibe o número atual da contagem
    print(cont)

    # Pausa de 1 segundo entre cada número
    sleep(1)

# Mensagem final exibida após o término da contagem
print("Feliz Ano Novo!!!🥳🎇🎆")
