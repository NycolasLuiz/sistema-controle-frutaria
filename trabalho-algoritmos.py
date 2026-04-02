import os
titulo = r"""
   ██████╗  ██████╗ ██████╗ ██████╗  ██████╗        ███████╗██████╗ ██╗   ██╗████████╗ █████╗ ███████╗
  ██╔════╝ ██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗       ██╔════╝██╔══██╗██║   ██║╚══██╔══╝██╔══██╗██╔════╝
  ██║  ███╗██║   ██║██████╔╝██║  ██║██║   ██║       █████╗  ██████╔╝██║   ██║   ██║   ███████║███████╗
  ██║   ██║██║   ██║██╔══██╗██║  ██║██║   ██║       ██╔══╝  ██╔══██╗██║   ██║   ██║   ██╔══██║╚════██║
  ╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝       ██║     ██║  ██║╚██████╔╝   ██║   ██║  ██║███████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝        ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝
"""


linha = "═" * 55

print(linha)
print(titulo)
input("Pressione ENTER para começar...")

os.system("cls" if os.name == "nt" else "clear")

print(linha)
print("MENU DE FRUTAS")
print(linha)
print("1 - Maçã")
print("2 - Banana")
print("3 - Pera")
print("4 - Uva")
print(linha)

# PRIMEIRA FRUTA
fruta1 = int(input("Escolha a primeira fruta: "))

if fruta1 == 1:
    nome1 = "maçã"
elif fruta1 == 2:
    nome1 = "banana"
elif fruta1 == 3:
    nome1 = "pera"
elif fruta1 == 4:
    nome1 = "uva"

peso1 = float(input(f"Peso da {nome1}: "))
valor1 = float(input(f"Valor da {nome1} (R$): "))

subtotal1 = peso1 * valor1

if peso1 >= 10:
    subtotal1 *= 0.90
elif peso1 >= 5:
    subtotal1 *= 0.95

print(linha)

# SEGUNDA FRUTA
fruta2 = int(input("Escolha a segunda fruta: "))

if fruta2 == 1:
    nome2 = "maçã"
elif fruta2 == 2:
    nome2 = "banana"
elif fruta2 == 3:
    nome2 = "pera"
elif fruta2 == 4:
    nome2 = "uva"

peso2 = float(input(f"Peso da {nome2}: "))
valor2 = float(input(f"Valor da {nome2} (R$): "))

subtotal2 = peso2 * valor2

if peso2 >= 10:
    subtotal2 *= 0.90
elif peso2 >= 5:
    subtotal2 *= 0.95

total = subtotal1 + subtotal2

print(linha)
pagamento = input("Pagamento à vista? (S/N): ").upper()

if pagamento == "S":
    total *= 0.95
    desconto_pagamento = "5%"
else:
    desconto_pagamento = "0%"

os.system("cls" if os.name == "nt" else "clear")

# RESUMO FINAL
print(linha)
print("RESUMO DA COMPRA")
print(linha)

print(f"{nome1.capitalize():<10} | {peso1:>5}kg | R$ {valor1:<6.2f}")
print(f"Subtotal: R$ {subtotal1:.2f}")

print("-" * 55)

print(f"{nome2.capitalize():<10} | {peso2:>5}kg | R$ {valor2:<6.2f}")
print(f"Subtotal: R$ {subtotal2:.2f}")

print("-" * 55)

print(f"Desconto pagamento: {desconto_pagamento}")
print(f"TOTAL FINAL: R$ {total:.2f}")

print(linha)
