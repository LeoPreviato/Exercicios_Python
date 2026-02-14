# Imprime um título centralizado com '=' ocupando 55 caracteres
print(" Dicionario em Python ".center(55, '='))

# Cria um dicionário vazio
dados = dict()

# Pede o nome do aluno, remove espaços extras e coloca a primeira letra maiúscula
dados['Nome'] = str(input("Nome: ")).strip().capitalize()

# Pede a média do aluno e já guarda no dicionário
dados['Média'] = float(input(f"Média de {dados['Nome']}: "))

# Linha separadora
print("=" * 55)

# Verifica se a média é maior ou igual a 7
if dados['Média'] >= 7:
    # Se for, adiciona ao dicionário a situação "Aprovado" em verde
    dados['Situação'] = '\033[1;32mAprovado\033[m'
else:
    # Caso contrário, adiciona "Reprovado" em vermelho
    dados['Situação'] = '\033[1;31mReprovado\033[m'

# Percorre todos os itens do dicionário
# pos recebe a chave (Nome, Média, Situação)
# v recebe o valor correspondente
for pos, v in dados.items():
    # Mostra cada chave com seu valor
    print(f"{pos} é igual a {v}.")

# Linha final
print("=" * 55)
