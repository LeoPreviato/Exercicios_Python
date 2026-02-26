# Título do programa centralizado com 55 caracteres usando "="
print(" Funções para Votação ".center(55, '='))

# Importa a classe date para pegar o ano atual do sistema
from datetime import date

# Importa sleep para criar pequenas pausas no programa
from time import sleep


def voto(nascimento):
    """
        -> Verifica a idade da pessoa e mostra na tela a sua situação para votar
        :param nascimento: Recebe o ano de nascimento da pessoa
        :return: Retorna de acordo com a idade se a pessoa pode votar, não pode ou voto opcional
        """
    idade = date.today().year - nascimento
    if 18 <= idade <= 69:
        return f"Você tem {idade} anos: SEU VOTO É OBRIGATÓRIO"
    elif 16 <= idade <= 17:
        return f"Você tem {idade} anos: NÃO PODE VOTAR"
    elif idade >= 70:
        return f"Você tem {idade} anos: VOTO OPCIONAL"

# Solicita ao usuário o ano de nascimento e converte para inteiro
ano_nascimento = int(input("Em que ano você nasceu? R: "))

# Pausa de 1 segundo para efeito visual
sleep(1)

# Mensagem indicando que o programa está processando
print("Analisando idade...")

# Outra pequena pausa
sleep(1)

# Chama a função voto() e imprime o valor retornado
print(voto(ano_nascimento))