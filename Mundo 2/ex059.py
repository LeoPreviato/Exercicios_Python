print(" Criando um Menu de Opções ".center(60, "="))

from time import sleep

opcao_usuario = 0

num1_usuario = int(input("Digite o primeiro número: "))
sleep(0.8)
num2_usuario = int(input("Digite o segundo número: "))

sleep(0.8)

while opcao_usuario != 5:
    print("-" * 40)
    print("Escolha uma das opções abaixo:")
    print("[1] Somar os dois números")
    print("[2] Multiplicar os dois números")
    print("[3] Qual o maior número")
    print("[4] Mudar os dois valores")
    print("[5] Sair do programa")
    print("-" * 40)
    sleep(1)
    opcao_usuario = int(input("Digite a sua escolha: "))

    print("-" * 40)

    print()

    if opcao_usuario == 1:
        soma = num1_usuario + num2_usuario
        print(f"A soma entre {num1_usuario} + {num2_usuario} é igual a {soma}")
        sleep(1)
        print()
    elif opcao_usuario == 2:
        multi = num1_usuario * num2_usuario
        print(f"A multiplicação entre {num1_usuario} x {num2_usuario} é igual a {multi}")
        sleep(1)
        print()
    elif opcao_usuario == 3:
        if num1_usuario > num2_usuario:
            print(f"O maior número é o {num1_usuario}")
            sleep(1)
            print()
        elif num2_usuario > num1_usuario:
            print(f"O maior múmero é o {num2_usuario}")
            sleep(1)
            print()
        else:
            print("Os dois números são iguais")
            sleep(1)
            print()
    elif opcao_usuario == 4:
        print("Digite novos números...")
        sleep(2)
        print()
        print("-" * 40)
        num1_usuario = int(input("Digite um novo número: "))
        sleep(0.8)
        num2_usuario = int(input("Digite um novo número: "))
    elif opcao_usuario == 5:
        print("Encerrando o programa...")
        sleep(1)
    else:
        print("Opção invalida. Digite novamente os números e sua escolha.")

print()

print("Fim do programa.")
