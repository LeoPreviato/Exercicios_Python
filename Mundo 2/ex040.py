# Imprime o título centralizado em 50 caracteres
print("=" * 50)
print("Aquele Classico da Média".center(50))
print("=" * 50)

# Importa a função sleep para criar pausas na execução do programa
from time import sleep

# Solicita ao usuário a primeira nota do aluno e converte para float
nota1 = float(input("Digite a primeira nota do aluno: "))

# Solicita ao usuário a segunda nota do aluno e converte para float
nota2 = float(input("Digite a segunda nota do aluno: "))

# Calcula a média aritmética das duas notas
media = (nota1 + nota2) / 2

# Pula uma linha para melhor organização visual
print()

# Exibe a média do aluno formatada com duas casas decimais
print(f"A sua média foi: {media:.2f}")

# Pausa o programa por 0.9 segundos
sleep(0.9)

# Pula outra linha
print()

# Verifica se a média é maior ou igual a 7
if media >= 7:
    # Exibe a mensagem de aprovação em verde
    print("Você foi \033[1;32mAPROVADO\033[m ✅, Parabéns!")

# Verifica se a média está entre 5.0 e 6.9 (recuperação)
elif 5.0 <= media <= 6.9:
    # Exibe a mensagem de recuperação em amarelo
    print("Você está de \033[1;33mRECUPERAÇÃO\033[m ⚠️, continue estudando!")

# Caso a média seja menor que 5.0
else:
    # Exibe a mensagem de reprovação em vermelho
    print("Você foi \033[1;31mREPROVADO\033[m ❌, estude mais da proxima vez!")
