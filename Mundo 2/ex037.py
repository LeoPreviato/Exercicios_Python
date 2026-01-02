# Importa a função sleep para pausar a execução do programa por alguns segundos
from time import sleep

# Imprime o título centralizado em um espaço de 45 caracteres
print("=" * 45)
print("Conversor de Bases Númericas".center(45))
print("=" * 45)

# Solicita ao usuário um número inteiro e converte a entrada para int
numero = int(input("Digite um número inteiro qualquer: "))

# Pausa o programa por 0.8 segundos para melhorar a experiência do usuário
sleep(0.8)

# Exibe o menu com as opções de conversão disponíveis
print("""
Escolha uma das três opções abaixo para fazer a conversão:
[ 1 ] Binario
[ 2 ] Octal
[ 3 ] Hexadecimal
""")

# Pausa novamente antes de pedir a escolha do usuário
sleep(0.8)

# Recebe a opção escolhida pelo usuário e converte para inteiro
opcao = int(input("Digite a sua escolha: "))

# Pequena pausa antes de executar a conversão
sleep(0.8)

# Verifica se a opção está entre 1 e 3
if opcao < 1 or opcao > 3:
    print("Opção invalida. Reinicie o programa novamente")

# Se estiver entre 1 e 3, ele vai começãr a conversão de acordo com a escolha
else:
    # Verifica se o usuário escolheu a opção Binário
    if opcao == 1:
        # Converte o número para binário usando a função bin()
        binario = bin(numero)
        # Exibe o resultado da conversão
        print(f"{numero} convertido para Binario: {binario[2:]}")

    # Verifica se o usuário escolheu a opção Octal
    elif opcao == 2:
        # Converte o número para octal usando a função oct()
        octal = oct(numero)
        # Exibe o resultado da conversão
        print(f"{numero} convertido para Octal: {octal[2:]}")

    # Caso a opção não seja 1 nem 2, o programa converte para Hexadecimal
    else:
        # Converte o número para hexadecimal usando a função hex()
        hexa = hex(numero)
        # Exibe o resultado da conversão
        print(f"{numero} convertido para Hexadecimal: {hexa[2:]}")
