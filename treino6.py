import os

def limpar_tela():
        input("Pressione Enter para limpar a tela.")
        os.system('cls')
        


reais = float(input("Qual valor você gostaria de converter: "))
dolar = 5.25
conversao = reais / dolar

if reais < 0:
    print("Coloque um número acima de US$00,00")
else:
    print(f"Esse valor em dolar é igual a: US${conversao:.2f}")
        
limpar_tela()

