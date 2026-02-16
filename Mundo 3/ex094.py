dados = dict()
lista_dici = list()
lista_mulheres = list()

while True:
    dados['Nome'] = str(input("Nome: ")).strip().capitalize()
    dados['Sexo'] = str(input("Sexo: ")).strip().upper()[0]
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input("Sexo invalido. Digite novamente [M/F]: ")).strip().upper()[0]

    dados['Idade'] = int(input("Idade: "))


    lista_dici.append(dados.copy())

    if dados['Sexo'] == 'F':
        lista_mulheres.append(dados['Nome'])

    opc = str(input("Quer continuar? [S/N]: ")).upper()[0]
    print("=" * 60)

    while opc not in 'SN':
        opc = str(input("Opção invalida. Digite novamente: ")).upper()[0]
        print("=" * 60)

    if opc == 'N':
        break

soma_idade = sum(p['Idade'] for p in lista_dici)

media_idade = soma_idade / len(lista_dici)

print(f"- O grupo tem {len(lista_dici)} pessoas.")

print(f"- A média de idade é de {media_idade:.2f} anos.")

print("- As mulheres cadastradas foram: ", end="")
for m in lista_mulheres:
    print(m, end=" ")
print()

print("- Lista das pessoas que estão acima da média:")

for p in lista_dici:
    if p['Idade'] > media_idade:
        print(f"Nome = {p['Nome']}; Sexo = {p['Sexo']}; Idade = {p['Idade']}")
        print()

print("Programa encerrado.")
