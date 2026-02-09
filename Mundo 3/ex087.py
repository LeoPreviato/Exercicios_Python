print(" Mais sobre matrix em Python ".center(45, '='))

lista_num = [[], [], []]

tot_pares = tot_terceira = 0

for l in range(0, 3):
    for c in range(0, 3):
        lista_num[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))

print("=" * 45)

for l in lista_num:
    for c in l:
        print(f"[  {c:^3}  ]", end=" ")
    print()

print("=" * 45)

# Soma dos valores pares
for p in lista_num:
    for v in p:
        if v % 2 == 0:
            tot_pares += v

print(f"A soma total dos valores pares é: {tot_pares}")

# Soma da terceira coluna (corrigido aqui)
for linha in lista_num:
    tot_terceira += linha[2]

print(f"A soma dos valores da terceira coluna é: {tot_terceira}")

# Maior valor da segunda linha
print(f"O maior valor da segunda linha é: {max(lista_num[1])}")
