print(" Validando expressão Matemáticas ".center(60, "="))

# Lê a expressão digitada pelo usuário e remove espaços nas pontas
expressao = str(input("Digite sua expressão: ")).strip()

# Lista usada como pilha para controlar parênteses abertos
pilha = []

# Percorre cada caractere da expressão
for exp in expressao:
    # Se encontrar um "(", empilha
    if exp == "(":
        pilha.append("(")

    # Se encontrar um ")", tenta desempilhar
    elif exp == ")":
        if len(pilha) > 0:
            # Existe um "(" aberto, então remove ele
            pilha.pop()
        else:
            # Não existe "(" para fechar: expressão inválida
            pilha.append("(")
            break

print('=' * 60)

# Se a pilha estiver vazia, todos os parênteses foram fechados corretamente
if len(pilha) == 0:
    print("Sua expressão é valida ✅")
else:
    print("Sua expressão não é valida ❌")
