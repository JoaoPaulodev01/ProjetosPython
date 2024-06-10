import os
def limpar_tela():
    os.system('cls')

limpar_tela()

reais = float(input("Qual valor você gostaria de converter: "))
dolar = 5.25
conversao = reais * dolar

if reais < 0:
    print("Coloque um número acima de R$00,00")
else:
    print(f"Esse valor em dolar é igual a: R${conversao:.2f}")

   
input("Pressione Enter para limpar a tela.")
limpar_tela()