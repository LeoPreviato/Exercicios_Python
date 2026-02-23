# Título do programa centralizado com 55 caracteres usando "="
print(" Função que descobre o Maior ".center(55, "="))

# Importa a função sleep para criar pequenas pausas
from time import sleep


# Função que apenas imprime uma linha de separação
def linha():
    print('=' * 55)


# Função contador recebe vários números (*num)
# O * permite receber quantos valores o usuário quiser
def contador(*num):

    # Mensagem inicial centralizada
    print("Analisando os valores passados...".center(55))

    # Chama a função linha
    linha()

    # Pausa de 0.7 segundos
    sleep(0.7)

    # Se nenhum valor foi passado
    if len(num) == 0:
        print("Foram informados 0 valores ao todo")
        print("O maior valor informado foi 0")

    # Se recebeu valores
    else:
        print("Os valores informados foram: ", end="")

        # Percorre todos os números recebidos
        for v in num:
            print(v, end=" ")

        # Mostra quantos valores foram informados
        print(f"\nForam informados ao todo {len(num)} valores")

        # Usa max() para descobrir o maior número
        print(f"O maior valor informado foi {max(num)}")

    # Pequena pausa
    sleep(0.8)

    # Linha final
    linha()


# Chamadas da função com quantidades diferentes de números
contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador()