# Imprime o título centralizado com 50 caracteres, preenchido com "="
print(" CLassificando Atletas ".center(50, "="))

# Importa a classe date para trabalhar com datas (ano atual)
from datetime import date

# Solicita o nome do atleta, remove espaços extras e deixa a primeira letra maiúscula
nome_atleta = str(input("Primeiro digite o seu nome: ")).strip().capitalize()

# Solicita o ano de nascimento do atleta
ano_nascimento = int(input("Agora digite o ano do seu nascimento: "))

# Calcula a idade do atleta com base no ano atual
idade = date.today().year - ano_nascimento

# Verifica se o atleta tem até 9 anos (categoria MIRIM)
if idade <= 9:
    print(f"{nome_atleta} de {idade} anos é da categoria: MIRIM")

# Verifica se o atleta tem até 14 anos (categoria INFANTIL)
elif idade <= 14:
    print(f"{nome_atleta} de {idade} anos é da categoria: INFANTIL")

# Verifica se o atleta tem até 19 anos (categoria JUNIOR)
elif idade <= 19:
    print(f"{nome_atleta} de {idade} anos é da categoria: JUNIOR")

# Verifica se o atleta tem exatamente 20 anos (categoria SÊNIOR)
elif idade == 20:
    print(f"{nome_atleta} de {idade} anos é da categoria: SÊNIOR")

# Caso o atleta tenha mais de 20 anos (categoria MASTER)
else:
    print(f"{nome_atleta} de {idade} anos é da categoria: MASTER")
