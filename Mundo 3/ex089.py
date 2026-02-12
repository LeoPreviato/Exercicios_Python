# Título do programa
print(" Boletim com listas Compostas ".center(55, "="))

# Lista principal: cada item será [nome, [nota1, nota2], média]
lista_prin = list()

# Cadastro dos alunos
while True:
    # Entrada de dados do aluno
    nome = str(input("Nome: ")).strip().capitalize()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2

    # Guarda os dados em uma lista composta
    lista_prin.append([nome, [n1, n2], media])

    # Pergunta se o usuário deseja continuar cadastrando
    opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    # Validação da opção
    while opcao not in "SN":
        opcao = str(input("Opção invalida. Digite denovo [S/N]: ")).strip().upper()[0]

    # Encerra o cadastro
    if opcao == "N":
        break

    print("=" * 55)

print("=" * 55)

# Cabeçalho do boletim resumido
print(f"{'No.':<4}{'NOME':<12}{'MÉDIA':>6}")

print("-" * 25)

# Mostra número, nome e média de cada aluno
for pos, n in enumerate(lista_prin):
    print(f"{pos:<4}{n[0]:<12}{n[2]:>6.1f}")

print("-" * 25)

# Consulta individual das notas
while True:
    print("=" * 55)
    nota_aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    # 999 finaliza a consulta
    if nota_aluno == 999:
        break
    else:
        # Mostra as duas notas do aluno escolhido
        print(f"Notas de {lista_prin[nota_aluno][0]} são: {lista_prin[nota_aluno][1]}")

print("Programa finalizado.")
