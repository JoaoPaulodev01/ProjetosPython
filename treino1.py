import os
def limpar_tela ():
    os.system('cls')

limpar_tela()

base = float(input("Qanto mede a base desse retângulo: (Em metros) "))
altura = float(input("Qanto mede a altura desse retângulo: (Em metros) "))
area = base*altura

if base < 0:
    print("Coloque um número acima de 0")
elif altura < 0:
    print("Coloque um número acima de 0")
else:
    print(f"A área desse retângulo é igual a: {area}m²")

input("Pressione Enter para limpar a tela.")
limpar_tela()
  