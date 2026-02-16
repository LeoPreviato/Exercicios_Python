# Título do programa centralizado
print(" Unindo dicionários e Listas ".center(60, '='))

# Dicionário temporário para guardar os dados de uma pessoa
dados = dict()

# Lista principal que vai armazenar todos os dicionários (todas as pessoas)
lista_dici = list()

# Lista para guardar apenas os nomes das mulheres
lista_mulheres = list()

# Laço infinito para cadastrar várias pessoas
while True:

    # Recebe o nome da pessoa
    dados['Nome'] = str(input("Nome: ")).strip().capitalize()

    # Recebe o sexo (pega só a primeira letra e transforma em maiúscula)
    dados['Sexo'] = str(input("Sexo: ")).strip().upper()[0]

    # Validação: só aceita M ou F
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input("Sexo invalido. Digite novamente [M/F]: ")).strip().upper()[0]
        print("=" * 60)

    # Recebe a idade
    dados['Idade'] = int(input("Idade: "))

    # Adiciona uma cópia do dicionário na lista principal
    # (copy é essencial para não sobrescrever os dados anteriores)
    lista_dici.append(dados.copy())

    # Se for mulher, adiciona o nome na lista de mulheres
    if dados['Sexo'] == 'F':
        lista_mulheres.append(dados['Nome'])

    # Pergunta se o usuário quer continuar cadastrando
    opc = str(input("Quer continuar? [S/N]: ")).upper()[0]
    print("=" * 60)

    # Validação da opção
    while opc not in 'SN':
        opc = str(input("Opção invalida. Digite novamente: ")).upper()[0]
        print("=" * 60)

    # Se escolher N, sai do laço
    if opc == 'N':
        break

# Soma todas as idades usando generator expression
soma_idade = sum(p['Idade'] for p in lista_dici)

# Calcula a média dividindo pela quantidade de pessoas
media_idade = soma_idade / len(lista_dici)

# Mostra quantas pessoas foram cadastradas
print(f"- O grupo tem {len(lista_dici)} pessoas.")

# Mostra a média de idade
print(f"- A média de idade é de {media_idade:.2f} anos.")

# Mostra todas as mulheres cadastradas
print("- As mulheres cadastradas foram: ", end="")
for m in lista_mulheres:
    print(m, end=" ")
print()

# Mostra as pessoas que estão acima da média
print("- Lista das pessoas que estão acima da média:")

for p in lista_dici:
    if p['Idade'] > media_idade:
        print(f"Nome = {p['Nome']}; Sexo = {p['Sexo']}; Idade = {p['Idade']}")
        print()

# Final do programa
print("Programa encerrado.")
