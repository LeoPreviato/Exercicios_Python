from datetime import date
# Importa a classe date para trabalhar com datas (vamos usar só o ano atual)

dados = dict()
# Cria um dicionário vazio para guardar todas as informações da pessoa

dados['Nome'] = str(input("Nome: ")).strip().capitalize()
# Pede o nome, remove espaços extras e deixa a primeira letra maiúscula
# Guarda no dicionário com a chave 'Nome'

ano_nasci = int(input("Ano de Nascimento: "))
# Pede o ano de nascimento e guarda numa variável

dados['Idade'] = date.today().year - ano_nasci
# Calcula a idade:
# ano atual - ano de nascimento
# e guarda no dicionário

dados['Ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
# Pede o número da carteira de trabalho
# se for 0, significa que não tem carteira

if dados['Ctps'] != 0:
    # Só entra aqui se a pessoa tiver carteira de trabalho

    dados['Contratação'] = int(input("Ano de Contratação: "))
    # Pede o ano em que a pessoa começou a trabalhar

    dados['Salário'] = float(input("Salário: R$"))
    # Pede o salário e guarda como float

    dados['Aposentadoria'] = dados['Idade'] + dados['Contratação'] + 35 - date.today().year
    # Calcula a idade da aposentadoria:
    # idade atual + (ano de contratação + 35 - ano atual)
    # ou seja:
    # calcula quantos anos faltam para completar 35 anos de trabalho
    # e soma com a idade atual

print("=" * 60)
# Apenas imprime uma linha decorativa

for k, v in dados.items():
    # Percorre cada chave (k) e valor (v) do dicionário

    print(f"{k} tem o valor: {v}")
    # Mostra cada dado armazenado
