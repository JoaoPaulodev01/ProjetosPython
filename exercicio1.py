import os
def limpar_tela():
    os.system('cls')

limpar_tela()

#variaveis
n1 = float(input ("Digite o primeiro número:"))
n2 = float(input ("Digite o segundo número:"))

#algoritmo
if n2 == 0:
   print("Não é possível dividir por 0")
elif n2 == 0:
   print("Não é possível dividir por 0")
else:
    print (f"Sua divisão é igual a {n1/n2}")

limpar_tela