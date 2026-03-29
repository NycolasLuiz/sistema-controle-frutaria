titulo = r"""
   ██████╗  ██████╗ ██████╗ ██████╗  ██████╗        ███████╗██████╗ ██╗   ██╗████████╗ █████╗ ███████╗
  ██╔════╝ ██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗       ██╔════╝██╔══██╗██║   ██║╚══██╔══╝██╔══██╗██╔════╝
  ██║  ███╗██║   ██║██████╔╝██║  ██║██║   ██║       █████╗  ██████╔╝██║   ██║   ██║   ███████║███████╗
  ██║   ██║██║   ██║██╔══██╗██║  ██║██║   ██║       ██╔══╝  ██╔══██╗██║   ██║   ██║   ██╔══██║╚════██║
  ╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝       ██║     ██║  ██║╚██████╔╝   ██║   ██║  ██║███████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝        ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝
"""

linha = "═" * 110 

print(linha)
print(titulo)
print(" " * 42 )
print(linha)
print("------------------")
print("| maça:   1      |")
print("| banana: 2      |")
print("| pera:   3      |")
print("| uva:    4      |")
print("------------------")
fruta1 = int(input("ESCOLHA A PRIMEIRA FRUTA:  "))

if(fruta1 == 1):
    pesoFruta1 = float(input("Insira o peso da maça:  "))
    valorFruta1=float(input("Insira o valor da maça  R$:  "))

if(fruta1 == 2):
    pesoFruta1 = float(input("Insira o peso da banana:  "))
    valorFruta1=float(input("Insira o valor da banana  R$:  "))
    
if(fruta1 == 3):
    pesoFruta1 = float(input("Insira o peso da pera:  "))
    valorFruta1=float(input("Insira o valor da pera  R$:  "))

if(fruta1 == 4):
    pesoFruta1 = float(input("Insira o peso da uva: "))
    valorFruta1=float(input("Insira o valor da uva  R$:  "))
    
valorTotalFruta1=pesoFruta1*valorFruta1
    
fruta2 = int(input("ESCOLHA A SEGUNDA FRUTA:  "))

if(fruta2 == 1):
    pesoFruta2 = float(input("Insira o peso da maça:  "))
    valorFruta2=float(input("Insira o valor da maça R$:  "))

if(fruta2 == 2):
    pesoFruta2 = float(input("Insira o peso da banana:  "))
    valorFruta2=float(input("Insira o valor da banana R$:  "))

if(fruta2 == 3):
    pesoFruta2 = float(input("Insira o peso da pera:  "))
    valorFruta2=float(input("Insira o valor da pera R$:  "))

if(fruta2 == 4):
    pesoFruta2 = float(input("Insira o peso da uva:  "))
    valorFruta2=float(input("Insira o valor da uva R$:  "))
    
valorTotalFruta2=pesoFruta2*valorFruta2

if pesoFruta1 >=5:
   valorTotalFruta1=valorTotalFruta1*0.95
    
elif pesoFruta2 >=10:
    valorTotalFruta2=valorTotalFruta2*0.90

resumoFinal=valorTotalFruta1+valorTotalFruta2
    
pagamento = input("Deseja pagar à vista para obter desconto? (S/N): ").upper()
        
print("╔════════════════════════════════════╗")

if pagamento == "S":
    print("║ PAGAMENTO À VISTA CONFIRMADO       ║")
    print("║ DESCONTO DE 50% APLICADO           ║")
    resumoFinal = resumoFinal * 0.5
else:
    print("║ PAGAMENTO NÃO FOI À VISTA          ║")
    print("║ DESCONTO NÃO APLICADO              ║")

print("╚════════════════════════════════════╝")


print(f"TOTAL A PAGAR: R$ {resumoFinal:.2f}")