import os

def menu_principal():
    """Exibe o menu principal com as opções disponíveis."""
    print('=' * 40)
    print('\033[1mMENU PRINCIPAL\033[m'.center(40))
    print('=' * 40)

    print('\033[32m1 - Ver pessoas Cadastradas\033[m')
    print('\033[33m2 - Cadastrar nova Pessoa\033[m')
    print('\033[35m3 - Sair do Programa\033[m')


def escolher_opcao():
    """Lê a opção do usuário e executa a ação correspondente.

    Valida entradas numéricas e direciona para cadastro, listagem ou
    encerramento do programa. Trata também opções inválidas.
    """
    try:
        opcao = int(input('\nDigite a sua opção: '))

        if opcao == 1:
            pessoas_cadastradas('pessoas_cadastradas.txt')
        elif opcao == 2:
            cadastrar_pessoa('pessoas_cadastradas.txt')
        elif opcao == 3:
            finalizar_programa()
        else:
            limpar_tela()
            opcao_invalida()

    except ValueError:
        limpar_tela()
        print('\033[31mERRO: por favor, digite um número.\033[m')
        voltar_ao_menu_principal()


def arquivo_existe(nome):
    """Verifica se o arquivo especificado existe.

    Args:
        nome (str): Caminho ou nome do arquivo a ser verificado.

    Returns:
        bool: True se o arquivo existe, False caso contrário.
    """
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """Cria um arquivo vazio com o nome fornecido.

    Args:
        nome (str): Caminho ou nome do arquivo a ser criado.
    """
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('\033[31mERRO: não consigo criar o arquivo\033[m')


def pessoas_cadastradas(nome):
    """Exibe na tela as pessoas cadastradas no arquivo.

    Args:
        nome (str): Caminho ou nome do arquivo de cadastro.
    """
    limpar_tela()
    try:
        arquivo = open(nome, 'rt')
    except:
        print('\033[31mERRO: não conseguo abrir esse arquivo.\033[m')
    else:
        print('=' * 30)
        print('\033[36mPESSOAS CADASTRADAS\033[m'.center(40))
        print('=' * 30)

        for linha in arquivo:
            dados = linha.split(';')

            if len(dados) < 2:
                continue

            nome_pessoa = dados[0]
            idade_pessoa = dados[1].replace('\n', '')

            print(f'{nome_pessoa:<20}{idade_pessoa:>3} anos')

        arquivo.close()
    voltar_ao_menu_principal()


def cadastrar_pessoa(arquivo):
    """Pede nome e idade e registra no arquivo de cadastro.

    Args:
        arquivo (str): Caminho ou nome do arquivo onde os dados serão
            adicionados.
    """
    limpar_tela()
    nome = input('\nNome: ').strip().title()
    idade = input('Idade: ').strip()

    try:
        arq = open(arquivo, 'at')
    except:
        print('\033[31mERRO: não consegui abrir esse arquivo\033[m')
    else:
        arq.write(f'{nome};{idade}\n')
        arq.close()
        print(f'\n"{nome}" foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def finalizar_programa():
    """Exibe mensagem de encerramento e finaliza o programa."""
    limpar_tela()
    print('Finalizando programa...\n')
    exit()


def opcao_invalida():
    """Informa que a opção é inválida e retorna ao menu principal."""
    print('\033[31mOpção invalida.\033[m')
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    """Pausa o programa até que o usuário pressione ENTER."""
    input('\nDigite ENTER para voltar para o menu principal')


def limpar_tela():
    """Limpa a tela do terminal usando o comando apropriado para o SO."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print()


def main():
    """Loop principal que exibe o menu e processa as escolhas do usuário."""
    arquivo = 'pessoas_cadastradas'
    
    if not arquivo_existe(arquivo):
        criar_arquivo(arquivo)
        
    while True:
        limpar_tela()
        menu_principal()
        escolher_opcao()
