# imprime uma linha de 40 caracteres '=' como separador visual
print("=" * 40)

# imprime o título 'Conversor de Temperaturas' centralizado em largura 40
print("Conversor de Temperaturas".center(40))

# imprime outra linha de separador
print("=" * 40)

# lê a temperatura em graus Celsius do usuário e converte a entrada (string) para float
temp_celsius = float(input("Digite a temperatura atual em ºC: "))

# converte Celsius para Fahrenheit pela fórmula (C * 9/5) + 32
conversao_para_far = (temp_celsius * 9/5) + 32

# exibe o resultado formatado mostrando a temperatura em ºC e em ºF
print(f"A temperatura de {temp_celsius}ºC, corresponde a {conversao_para_far}ºF!")
