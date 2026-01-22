from random import randint
from time import sleep

# Título do jogo centralizado
print(" Jogo do Ímpar ou Par ".center(60, "="))

# Contador de vitórias consecutivas
tot_vitoria = 0

# Loop principal do jogo
while True:
    # Jogador escolhe um número
    num_jogador = int(input("Digite um número: "))

    # Jogador escolhe Par ou Ímpar
    opcao_jogador = str(
        input("Você escolhe Par ou ímpar? [P/I]: ")).strip().upper()[0]

    # Validação da escolha do jogador
    if opcao_jogador != "P" and opcao_jogador != "I":
        sleep(1)
        while True:
            if opcao_jogador != "P" and opcao_jogador != "I":
                print("-" * 60)
                opcao_jogador = str(
                    input("Opção inválida. Digite novamente [P/I]: ")).strip().upper()[0]
                sleep(0.8)
            else:
                break

    sleep(1)
    print("=" * 60)

    # Número aleatório do computador
    num_computador = randint(1, 10)

    # Soma dos valores
    soma = num_jogador + num_computador

    # Exibição do resultado da rodada
    print(
        f"Você jogou {num_jogador} e o computador jogou {num_computador}. "
        f"Total de {soma}, ",
        end=""
    )

    # Verificação se deu par ou ímpar
    if soma % 2 == 0:
        print("deu Par!")
    else:
        print("deu Ímpar!")

    print("=" * 60)
    sleep(1)

    # Lógica de vitória ou derrota
    if opcao_jogador == "P":
        if soma % 2 == 0:
            tot_vitoria += 1
            print("\033[1;32mVocê venceu!!!\033[m")
            print("🔥 Vamos para a próxima rodada!")
            print(f"🏆 Vitórias consecutivas: {tot_vitoria}")
            print("=" * 60)
        else:
            print("\033[1;31mVocê perdeu!\033[m")
            break
    else:
        if soma % 2 != 0:
            tot_vitoria += 1
            print("\033[1;32mVocê venceu!!!\033[m")
            print("🔥 Vamos para a próxima rodada!")
            print(f"🏆 Vitórias consecutivas: {tot_vitoria}")
            print("=" * 60)
        else:
            print("\033[1;31mVocê perdeu!\033[m")
            break

# Mensagem final do jogo
sleep(1)
print("=" * 60)
print("\033[1;31mGAME OVER.\033[m")
sleep(1)
print(f"\033[1mVocê venceu {tot_vitoria} vezes seguidas!\033[m")
print("=" * 60)
