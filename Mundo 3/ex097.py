# Exibe uma linha separadora fixa no terminal.
def linha():
    print("-" * 55)


# Mostra uma mensagem centralizada dentro de uma "moldura" de "=".
def mensagem(texto):
    # Define a largura da moldura com base no tamanho do texto.
    tamanho_plv = len(texto)+4
    
    print("="* tamanho_plv)
    print(texto.center(tamanho_plv))
    print("="* tamanho_plv)
    

# Laço principal do programa.
while True:
    # Lê o texto do usuário, removendo espaços extras e padronizando em maiúsculas.
    texto = str(input("Digite uma palavra qualquer: ")).strip().upper()
    
    # Exibe o texto formatado.
    mensagem(texto)
    
    # Pergunta se o usuário deseja continuar.
    opc = str(input("Quer continuar? [S/N]: ")).strip().upper()
    
    linha()
    
    # Valida a entrada: aceita apenas S ou N.
    while opc == "" or opc[0] not in "SN":
        linha()
        opc = input("Opção invalida. Digite novamente: ").strip().upper()
        
    # Considera apenas o primeiro caractere digitado.
    opc = opc[0]
    
    # Encerra o programa se a opção for N.
    if opc == "N":
        break

# Mensagem final após sair do laço.
print("Programa encerrado.")
