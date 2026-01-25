# Exibe o título do programa centralizado com 60 caracteres
print(" Estatísticas em Produtos ".center(60, "="))

# Variáveis:
# tot_valor → soma total dos preços
# pdt_mais1000 → contador de produtos acima de R$1000
# pdt_maisBarato → guarda o menor preço encontrado
tot_valor = pdt_mais1000 = pdt_maisBarato = 0

# Guarda o nome do produto mais barato
nome_pdt_barato = ""

# Loop principal do programa
while True:
    # Lê o nome do produto e remove espaços extras, deixando em maiúsculo
    nome_produto = str(input("Digite o nome do produto: ")).strip().upper()

    # Lê o preço do produto
    preco_produto = float(input("Agora digite o preço desse produto: R$"))

    # Soma o preço ao total da compra
    tot_valor += preco_produto

    print("=" * 60)

    # Verifica se o produto custa mais de R$1000
    if preco_produto > 1000:
        pdt_mais1000 += 1

    # Verifica se é o primeiro produto
    # ou se o preço atual é menor que o menor preço registrado
    if pdt_maisBarato == 0 or preco_produto < pdt_maisBarato:
        pdt_maisBarato = preco_produto
        nome_pdt_barato = nome_produto

    # Pergunta ao usuário se deseja continuar
    opcao = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]

    print("=" * 60)

    # Validação da opção digitada
    while opcao not in "SN":
        opcao = str(
            input("\033[1;31mOpção inválida.❌\033[m \033[1mDigite novamente [S/N]:\033[m ")
        ).strip().upper()[0]

        print("=" * 60)

    # Confirmação de cadastro do produto
    print(f"\033[1;32m{nome_produto} CADASTRADO COM SUCESSO\033[m✅".center(60))
    print("=" * 60)

    # Encerra o loop caso o usuário não queira continuar
    if opcao == "N":
        break

# Fim do programa
print("\033[1;33mFim do programa\033[m".center(60))
print("=" * 60)

# Exibe os resultados finais
print(f"O total da sua compra foi de R${tot_valor:.2f}")
print(f"Temos {pdt_mais1000} produtos acima de R$1000")
print(f"E o produto mais barato foi {nome_pdt_barato}, que custou R${pdt_maisBarato:.2f}")
