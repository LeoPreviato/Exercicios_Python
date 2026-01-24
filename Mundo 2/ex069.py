# Título do programa centralizado
print(" Analise de Dados do Grupo ".center(60, "="))
print()

# Contadores:
# tot_mais18 → pessoas com 18 anos ou mais
# tot_homens → total de homens cadastrados
# mulheres_menos20 → mulheres com menos de 20 anos
tot_mais18 = tot_homens = mulheres_menos20 = 0

# Loop principal do programa
while True:
    print("=" * 60)
    print("\033[1;33mCADASTRE UMA PESSOA\033[m".center(60))
    print("=" * 60)

    # Entrada da idade
    idade = int(input("Digite a sua idade: "))

    # Entrada do sexo (pega só a primeira letra e coloca em maiúsculo)
    sexo = str(input("Agora digite o seu sexo [M/F]: ")).strip().upper()[0]
    print("=" * 60)

    # Validação do sexo
    # Enquanto não for M ou F, pede novamente
    while sexo not in "MF":
        sexo = str(
            input("\33[1;31mSexo invalido.\033[m "
                  "\033[1mDigite novamente o seu sexo [M/F]:\033[m ")).strip().upper()[0]
        print("=" * 60)

    # Conta pessoas com 18 anos ou mais
    if idade >= 18:
        tot_mais18 += 1

    # Conta homens cadastrados
    if sexo == "M":
        tot_homens += 1

    # Conta mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        mulheres_menos20 += 1

    # Confirmação de cadastro
    print("\033[1;32mPESSOA CADASTRADA COM SUCESSO!\033[m".center(60))
    print("=" * 60)

    # Pergunta se o usuário quer continuar
    opcao = str(input("Você quer continuar cadastrando? [S/N]: ")).strip().upper()[0]

    # Validação da opção
    while opcao not in "SN":
        print("=" * 60)
        opcao = str(
            input("\033[1;31mOpção invalida.\033[m "
                  "\033[1mDigite novamente [S/N]:\033[m ")
        ).strip().upper()[0]

    # Se escolher N, encerra o loop
    if opcao == "N":
        break

# Resultado final
print("=" * 60)
print(f"Ao total teve {tot_mais18} pessoas com mais de 18 anos no cadastro. 🔞")
print()
print(f"{tot_homens} homens foram cadastrados 🚹")
print()
print(f"{mulheres_menos20} mulheres com menos de 20 anos no cadastro. 🚺")
