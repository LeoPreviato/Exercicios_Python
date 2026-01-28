# Título do programa, centralizado em 65 caracteres usando "="
print(" Ánalise de Dados em uma Tupla ".center(65, "="))


# Tupla vazia que será usada para armazenar os números pares digitados
nums_pares = ()


# Cria uma tupla com 4 valores digitados pelo usuário
# Cada valor é convertido para inteiro
valores_tupla = (
    int(input("Digite o primeiro valor: ")),
    int(input("Digite o segundo valor: ")),
    int(input("Digite o terceiro valor: ")),
    int(input("Digite o quarto valor: "))
)


# Linha separadora
print("=" * 65)


# Mostra todos os valores digitados pelo usuário
print(f"Você digitou os valores: {valores_tupla}")


# Linha separadora
print("=" * 65)


# Mostra quantas vezes o número 9 apareceu na tupla
# count() conta a quantidade de ocorrências do valor informado
print(f"O valor 9 apareceu {valores_tupla.count(9)} vezes")


# Linha separadora
print("=" * 65)


# Verifica se o número 3 está presente na tupla
if 3 in valores_tupla:
    # index() retorna a posição da primeira ocorrência do número 3
    # +1 é usado para mostrar a posição correta (começando em 1)
    print(f"O valor 3 apareceu na {valores_tupla.index(3)+1}ª posição")
else:
    # Caso o número 3 não tenha sido digitado
    print("O valor 3 não foi digitado em nenhuma posição!")


# Linha separadora
print("=" * 65)


# Percorre a tupla para identificar os números pares
for n in valores_tupla:
    # Verifica se o número é par
    if n % 2 == 0:
        # Adiciona o número par à tupla nums_pares
        # Como tuplas são imutáveis, é feita a concatenação
        nums_pares += (n, )


# Verifica se existe ao menos um número par armazenado
if nums_pares:
    print(f"Os números PARES digitados foram: ", end="")
    # Mostra todos os números pares encontrados
    for numeros in nums_pares:
        print(numeros, end=" ")
else:
    # Caso nenhum número par tenha sido digitado
    print("Nenhum número PAR foi digitado!")


# Linha separadora
print("=" * 65)


# Mensagem final do programa
print("Fim do Programa.")
