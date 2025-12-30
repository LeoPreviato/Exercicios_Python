# Importa a função sleep para criar pausas entre as mensagens
from time import sleep

# Exibe o título centralizado com caracteres "="
print(" Gerenciador de Pagamentos ".center(45, "="))

# Solicita o nome do usuário, remove espaços extras e deixa a primeira letra maiúscula
nome_usuario = str(input("Primeiro digite o seu nome: ")).strip().capitalize()

# Pequena pausa para melhorar a experiência do usuário
sleep(0.8)

# Solicita o preço do produto e converte para float
preco_produto = float(input("Agora digite o preço do produto: R$"))

# Pausa
sleep(0.8)

# Exibe o menu com as opções de pagamento
print("""
Escolha o método de pagamento abaixo:
[1] À vista dinheiro/cheque💵: 10% de desconto
[2] À vista no cartão💳: 5% de desconto
[3] Em até 2x no cartão💳: preço normal
[4] 3x ou mais no cartão💳: 20% de juros
""")

# Pausa
sleep(0.8)

# Recebe a opção de pagamento escolhida pelo usuário
opcao_pagamento = int(input("Digite a sua opção de pagamento: "))

print()

# Pausa
sleep(0.8)

# Verifica se a opção digitada é inválida
if opcao_pagamento < 1 or opcao_pagamento > 4:
    print(f"Não existe o metodo {opcao_pagamento} nas opções de pagamento❌.")
    sleep(0.8)
    print("Digite seu nome, o preço do produto e sua opção de pagamento novamente!✅")

# Caso a opção seja válida
else:
    # Opção 1: pagamento à vista com 10% de desconto
    if opcao_pagamento == 1:
        desconto_10 = preco_produto * 0.90
        print(f"{nome_usuario} o preço final do seu produto será de R${desconto_10:.2f}!")

    # Opção 2: pagamento à vista no cartão com 5% de desconto
    elif opcao_pagamento == 2:
        desconto_5 = preco_produto * 0.95
        print(f"{nome_usuario} o preço final do seu produto será de R${desconto_5:.2f}!")

    # Opção 3: pagamento em até 2x sem juros
    elif opcao_pagamento == 3:
        print(f"{nome_usuario} o preço do seu produto não irá mudar, continuará R${preco_produto}!")

    # Opção 4: pagamento em 3x ou mais com 20% de juros
    elif opcao_pagamento == 4:
        # Calcula o valor total com juros apenas uma vez
        juros = preco_produto * 1.20

        # Solicita a quantidade de parcelas
        vezes_pagar = int(input("Você vai fazer em 3x ou mais?: "))

        # Caso seja exatamente 3 parcelas
        if vezes_pagar == 3:
            parcela = juros / 3
            print(f"Será 3x de R${parcela:.2f}, valor final será R${juros:.2f}!")

        # Caso seja entre 4 e 12 parcelas
        elif 4 <= vezes_pagar <= 12:
            parcela = juros / vezes_pagar
            print(f"Será em {vezes_pagar}x de R${parcela:.2f}, valor final será R${juros:.2f}!")

        # Caso o número de parcelas seja inválido
        else:
            print("Número de parcelas invalido❌. Escolha entre 3 e 12.")
