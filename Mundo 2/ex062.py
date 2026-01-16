# Exibe o título do programa centralizado
print(" Progressão Aritmética V.3.0 ".center(50, "="))

# Solicita ao usuário o primeiro termo da progressão aritmética
primeiro_termo = int(input("Digite o primeiro termo da PA: "))

# Solicita ao usuário a razão da progressão aritmética
razao = int(input("Agora digite a razão: "))

# A variável PA começa com o primeiro termo informado
PA = primeiro_termo

# Contador que controla quantos termos já foram mostrados
cont = 1

# Variável que guarda o total de termos exibidos até agora
total = 0

# Quantidade inicial de termos que serão mostrados (começa com 10)
mais_termos = 10

# Enquanto o usuário não digitar 0, o programa continua
while mais_termos != 0:

    # Soma a nova quantidade de termos ao total já exibido
    total += mais_termos

    # Laço interno responsável por exibir os termos da PA
    # Ele continua até atingir o total de termos desejado
    while cont <= total:
        # Mostra o termo atual da progressão
        print(PA, end=" → ")

        # Calcula o próximo termo da PA somando a razão
        PA += razao

        # Incrementa o contador de termos exibidos
        cont += 1

    # Pausa visual entre os blocos de termos
    print("Pausa")
    print()

    # Pergunta ao usuário quantos termos a mais ele quer ver
    mais_termos = int(input("Você quer ver mais quantos termos: "))

# Linha em branco para organização da saída
print()

# Mensagem final informando quantos termos foram exibidos no total
print(f"Fim da Progressão Aritmética, você viu ao todo {total} termos")
