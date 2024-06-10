import os
def limpar_tela():
    os.system('cls')

limpar_tela()

valor = float(input("Qual o valor do produto: (Em reais): "))
desconto = float(input("Qual a porcentagem de desconto para esse produto: "))
porcentagem = desconto/100 * valor
preco = valor - desconto

if valor < 0:
    print("Coloque um número acima de R$00,00")
elif desconto < 0:
    print("Coloque um número acima de 0%")
else:
    print(f"O valor final do produto é igual a R${preco:.2f}")

input("Pressione Enter para limpar a tela.")
limpar_tela()