# Imprime o título centralizado com 65 caracteres e preenchido com "="
print(" Contando Vogais Em Tupla ".center(65, "="))

# Tupla com várias palavras que serão analisadas
palavras = (
    'aprender', 'programar', 'linguagem', 'python', 'curso',
    'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
    'programador', 'futuro'
)

# Laço que percorre cada palavra da tupla 'palavras'
for p in palavras:
    # Mostra a palavra em maiúsculas
    print(f"\nNa palavra {p.upper()} temos: ", end="")

    # Laço que percorre cada letra da palavra atual
    for v in p:
        # Verifica se a letra é uma vogal
        if v in 'aeiou':
            # Imprime a vogal encontrada, sem pular linha
            print(v, end=" ")
