# Exibe o título do programa centralizado
print(" Progressão Aritmética V.2.0 ".center(50, "="))

# Solicita ao usuário o primeiro termo da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))

# Solicita ao usuário a razão da PA
razao = int(input("Agora digite a razão da PA: "))

# A variável PA começa com o primeiro termo informado
PA = primeiro_termo

# Contador para controlar a quantidade de termos exibidos
cont = 1

# Enquanto o contador for menor ou igual a 10,
# o laço continuará mostrando os termos da progressão
while cont <= 10:
    # Mostra o termo atual da PA
    print(PA, end=" → ")

    # Soma a razão ao termo atual para gerar o próximo termo
    PA += razao

    # Incrementa o contador
    cont += 1

# Mensagem final indicando o fim da progressão
print("Fim da Progressão Aritmética")
