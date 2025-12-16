# Imprime uma linha de 55 caracteres '='
print("=" * 55)
# Centraliza o título em 55 caracteres
print("Primeira e ultima ocorrencia de uma string".center(55))
# Imprime outra linha de 55 caracteres '='
print("=" * 55)

# Solicita ao usuário uma frase, remove espaços em branco nas extremidades e converte para minúsculas
frase = str(input("Digite uma frase qualquer: ")).strip().lower()

# Conta quantas vezes a letra 'a' aparece na frase e exibe o resultado
print(f"A letra 'A' aparece {frase.count('a')} vezes na frase")

# Encontra a posição da primeira ocorrência da letra 'a' (sum 1 porque índices começam em 0) e exibe
print(f"A letra 'A' aparece pela primeira vez na {frase.find('a')+1} posição")

# Encontra a posição da última ocorrência da letra 'a' (sum 1 porque índices começam em 0) e exibe
print(f"E ela aparece pela ultima vez na {frase.rfind('a')+1} posição")
