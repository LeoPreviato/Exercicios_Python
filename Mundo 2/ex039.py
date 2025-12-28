# Imprime o título centralizado em 35 caracteres
print("=" * 35)
print("Alistamento Milítar".center(35))
print("=" * 35)

# Importa a classe date para trabalhar com datas (ano atual)
from datetime import date

# Importa a função sleep para criar pausas no programa
from time import sleep

# Pede ao usuário o ano de nascimento e converte para inteiro
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Pula uma linha para melhorar a aparência no terminal
print()

# Pausa o programa por 0.9 segundos
sleep(0.9)

# Calcula a idade subtraindo o ano de nascimento do ano atual
idade = date.today().year - ano_nascimento

# Verifica se o usuário tem menos de 18 anos
if idade < 18:
    # Mostra a idade atual
    print(f"Você tem {idade} anos de idade, ", end="")
    sleep(0.9)

    # Mostra quantos anos faltam para o alistamento
    print(f"ainda faltam {18 - idade} anos para você se alistar!")

# Verifica se o usuário tem mais de 18 anos
elif idade > 18:
    # Pergunta se o usuário já se alistou e converte a resposta para maiúscula
    pergunta_usuario = str(input("Você tem mais de 18 anos, você ja se alistou? [S/N]: ")).upper()
    print()
    sleep(0.9)

    # Se a resposta for "S"
    if pergunta_usuario == "S":
        # Informa que não é necessário se alistar novamente
        print(f"Já que você ja se alistou, não será necessario se alistar novamente.")
        sleep(0.9)
        print("Tenha um bom dia!")

    # Caso a resposta seja diferente de "S"
    else:
        # Mostra quantos anos já se passaram do período correto de alistamento
        print(f"Já se passaram {idade - 18} anos do seu alistamento.")
        sleep(0.9)

        # Orienta o usuário a procurar uma Junta Militar
        print(f"Corra para uma Junta Milítar mais proxima.")

# Caso o usuário tenha exatamente 18 anos
else:
    # Informa que ele está na idade correta para se alistar
    print(f"Você tem {idade} anos de idade e está na idade certa para se alistar!")
    sleep(0.9)

    # Orienta o usuário a ir até a Junta Militar
    print(f"Vá para a Junta Milítar mais proxima.")
