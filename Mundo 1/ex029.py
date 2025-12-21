from time import sleep  # importa sleep para pausar a execução por alguns segundos

# cabeçalho visual
print("=" * 25)  # imprime 25 sinais de igual
print("Radar eletrónico".center(25))  # centraliza o título em um campo de 25 caracteres
print("=" * 25)

# lê a velocidade informada pelo usuário e converte para inteiro
velocidade_carro = int(input("Digite a velocidade que o carro estava: "))
sleep(1)  # pequena pausa para melhor leitura das mensagens

# verifica se a velocidade excede o limite de 80 km/h
if velocidade_carro > 80:
    # calcula o valor da multa: R$7,00 por km acima do limite
    multa = (velocidade_carro - 80) * 7
    print("Você foi MULTADO!")
    sleep(1)
    # informa o motivo e o valor da multa com formatação de duas casas decimais
    print("Você ultrapassou o limite de 80km/h, ", end="")
    print(f"portanto será multado em R${multa:.2f}!")
else:
    # caso não ultrapasse o limite, mensagem de conformidade
    print("Você está dentro do limite de velocidade.")
    sleep(1)
    print("Boa viajem!")
