# Mostra um título centralizado com '='
print(" Função que calcula a Área ".center(55, '='))


# Criação da função 'area' com dois parâmetros:
# larg = largura do terreno
# compri = comprimento do terreno
def area(larg, compri):
    # Calcula a área multiplicando largura pelo comprimento
    a = larg * compri

    # Mostra o resultado formatado na tela
    print(f"A área do seu terreno de {larg}x{compri} é de {a}m²")


# Pede para a pessoa a largura do terreno (em metros)
# Converte para float porque pode ter casas decimais
larg = float(input("Digite a LARGURA (m) do seu terreno: "))

# Pede o comprimento do terreno (em metros)
compri = float(input("Agora digite o COMPRIMEIRO (m) do seu terreno: "))

# Linha decorativa
print('=' * 55)

# Chama a função 'area' passando os valores digitados
# Esses valores entram nos parâmetros larg e compri
area(larg, compri)
