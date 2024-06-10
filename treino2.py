import os
def limpar_tela():
    os.system('cls')

limpar_tela()

lado = float(input("Quanto mede os lados desse quadrado: "))
area = lado ** 2

if lado < 0:
    print("Coloque um número acima de 0")
else:
    print(f"A área desse quadrado é igual a: {area}m²")

input("Pressione Enter para limpar a tela.")
limpar_tela()
