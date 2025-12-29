# Importa a função sleep para criar pequenas pausas no programa
from time import sleep

# Exibe um título centralizado com 55 caracteres, preenchendo com '='
print(" Índice de Massa Corporal ".center(55, "="))

# Solicita a altura do usuário (em metros) e converte para float
altura = float(input("Primeiro digite sua altura: "))
sleep(0.8)  # Pausa para melhorar a experiência do usuário

# Solicita o peso do usuário (em kg) e converte para float
peso = float(input("Agora digite o seu peso: "))
sleep(0.8)

# Calcula o IMC usando a fórmula: peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

# Linha em branco para melhor organização visual
print()

# Exibe o valor do IMC com duas casas decimais
print(f"Seu IMC é de: {imc:.2f}")
sleep(0.8)

print()

# Estrutura condicional para classificar o IMC
if imc < 18.5:
    # Se chegou aqui, o IMC é menor que 18.5
    print("Você está muito abaixo do peso.")
    sleep(0.8)
    print("Procure se alimentar melhor!🥩🍖")

elif imc < 25:
    # Se chegou aqui, o IMC é maior ou igual a 18.5
    print("Você está no peso ideal. Parabéns!👏🏻🚀")

elif imc < 30:
    # Se chegou aqui, o IMC está entre 25 e 29.9
    print("Você está com sobrepeso.")
    sleep(0.8)
    print("Procure fazer exercícios!🏃🏼🏃🏼‍♀️")

elif imc < 40:
    # Se chegou aqui, o IMC está entre 30 e 39.9
    print("Você tem obesidade.")
    sleep(0.8)
    print("Procure se alimentar melhor!🍎🍉")

else:
    # Caso o IMC seja 40 ou maior
    print("Você tem obesidade mórbida.")
    sleep(0.8)
    print("Procure ajuda médica e acompanhamento profissional.👨🏻‍⚕️🚑")
