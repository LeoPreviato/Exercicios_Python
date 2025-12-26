# Importa a função sleep do módulo time para criar pausas na execução
from time import sleep

# Imprime um cabeçalho decorativo com linhas de "=" e o título centralizado
print("=" * 40)
print("Aprovando Empréstimos".center(40))
print("=" * 40)

# Solicita ao usuário o valor da casa (em reais) e converte para inteiro
valor_casa = int(input("Digite o valor da casa que você deseja comprar: R$"))
# Pausa de 0.7 segundos para efeito dramático
sleep(0.7)
# Solicita o salário do comprador e converte para float (permite centavos)
salario_comprador = float(input("Digite o seu salário: R$"))
sleep(0.7)
# Solicita o número de anos para pagar e converte para inteiro
anos_pagar = int(input("Agora digite em quantos anos você deseja pagar: "))
sleep(0.7)

# Calcula o total de meses multiplicando anos por 12
meses = anos_pagar * 12

# Calcula a prestação mensal dividindo o valor da casa pelo número de meses
# Nota: Isso assume prestação fixa sem juros; em empréstimos reais, há juros
prestacao = valor_casa / meses

# Calcula o limite de 30% do salário mensal
limite_salario = salario_comprador * 0.30

# Verifica se a prestação excede o limite do salário
if prestacao > limite_salario:
    # Imprime mensagem de negação em vermelho (usando códigos ANSI) com emoji
    print("Empréstimo \033[1;31mNEGADO!\033[m❌")
    sleep(1)
    # Explica o motivo da negação
    print("A prestação excedeu 30% do seu salário")
# Verifica se a prestação é menor que o limite (aprovação)
else:
    # Imprime mensagem de aprovação em verde com emoji
    print("Empréstimo \033[1;32mAPROVADO!\033[m✅")
    sleep(1)
    # Mostra os detalhes da prestação formatados com 2 casas decimais
    print(f"Você terá que pagar R${prestacao:.2f} por mes em {anos_pagar} anos.")
