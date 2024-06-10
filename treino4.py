import os
def limpar_tela():
    os.system('cls')

limpar_tela()

raio = float(input("Quanto mede o raio desse círculo: "))
area = 3.141592 * raio ** 2

if raio < 0:
    print("Coloque um número acima de 0")
else:
    print(f"A área desse círculo o é igual a: {area}m²")

input("Pressione Enter para limpar a tela.")
limpar_tela()