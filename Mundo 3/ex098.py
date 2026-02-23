# Centraliza o título com = em volta
print(" Função de Contador ".center(55, '='))

# Importa a função sleep para criar pausas
from time import sleep


# Função só para imprimir uma linha separadora
def linha():
    print("=" * 55)


# Função principal do contador
def contador(inicio, fim, passo):
    # Se o passo for negativo, transforma em positivo
    if passo < 0:
        passo = abs(passo)

    # Se o passo for zero, vira 1 para evitar erro no range
    elif passo == 0:
        passo += 1

    # Caso a contagem seja regressiva (ex: 10 até 0)
    if inicio > fim:
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

        # range começa em inicio, vai até fim-1 e anda negativo
        for v in range(inicio, fim - 1, -passo):
            print(v, end=" ", flush=True) # flush=True - força a saída imediata no terminal
            sleep(0.5)

    # Caso a contagem seja progressiva (ex: 1 até 10)
    elif inicio < fim:
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

        # range começa em inicio, vai até fim+1 e anda positivo
        for v in range(inicio, fim + 1, passo):
            print(v, end=" ", flush=True)
            sleep(0.5)

    # Caso inicio seja igual ao fim
    else:
        print(inicio)

    # Mensagem final
    print("Fim!")

    # Chama a função linha para separar visualmente
    linha()


# Testes automáticos
contador(1, 10, 1)
contador(10, 0, 2)

# Mensagem para o usuário
print("Agora é a sua vez de personalizar contagem!")

# Entrada dos valores pelo teclado
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

# Linha separadora
linha()

# Chamada do contador com valores do usuário
contador(inicio, fim, passo)