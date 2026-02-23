# Importa a função randint para gerar números aleatórios
from random import randint

# Importa sleep para criar pequenas pausas na execução
from time import sleep


# Lista global com 5 números sorteados entre 1 e 10
lista_num = [
    randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10)
]


# Função responsável por mostrar os números sorteados
def sorteio():
    print("Sorteando 5 valores para a lista: ", end="")

    # Percorre cada valor da lista
    for v in lista_num:
        sleep(0.4)           # pequena pausa antes de mostrar
        print(v, end=" ", flush=True)    # imprime na mesma linha
        sleep(0.4)           # pausa depois de mostrar

    print("PRONTO!")         # mensagem final


# Função responsável por somar apenas os valores pares da lista
def soma():
    s = 0  # variável local que acumula a soma dos pares

    # Percorre cada número da lista
    for p in lista_num:
        # Verifica se o número é par
        if p % 2 == 0:
            s += p  # adiciona na soma

    sleep(1)  # pausa antes de mostrar resultado

    # Mostra o resultado final
    print(f"Somando os valores pares de {lista_num}, temos {s}")


# Chamada das funções
sorteio()
soma()