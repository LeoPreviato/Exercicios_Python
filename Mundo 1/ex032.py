# Exibe uma linha de separação com 30 sinais de igual
print("=" * 30)
print("Ano Bissexto".center(30))
print("=" * 30)

# Lê o ano informado pelo usuário e converte para inteiro
ano = int(input("Digite um ano para saber se é bissexto ou não: "))

# Condição de ano bissexto:
# - é bissexto se for divisível por 4 e não for divisível por 100
# - exceto se for divisível por 400 (aí também é bissexto)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Imprime resultado quando é bissexto
    print(f"O ano {ano} é bissexto!")
else:
    # Imprime resultado quando não é bissexto
    print(f"O ano {ano} não é bissexto!")
