"""Conversor simples de metros para centímetros e milímetros.

O programa solicita uma medida em metros e exibe o valor equivalente
em centímetros e em milímetros.
"""

# Usamos float para aceitar medidas com casa decimal (ex: 1.5 m)
medida_usu = float(input("Digite uma medida em metros (ex: 1.5): "))

# Converte metros para centímetros (1 m = 100 cm)
cm = medida_usu * 100

# Converte metros para milímetros (1 m = 1000 mm)
mm = medida_usu * 1000

# Exibe os resultados. Formatação: se quiser, podemos controlar casas decimais.
print(f"{medida_usu} m convertido para centímetros é {cm} cm.")
print(f"{medida_usu} m convertido para milímetros é {mm} mm.")
