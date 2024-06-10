#limpar tela

import os
def limpar_tela():
    os.system('cls')

limpar_tela()

#atividade 1

def Atividade1():

#variaveis
  letra = input("Qual letra você deseja analisar:").lower()

#teste logico
  if letra.isalpha():
   if letra in "a, e, i, o, u":
    print(f"A letra {letra} é uma vogal. ")
   else:
    print(f"A letra {letra} é uma consoante. ")
  else:
    print("Digite apenas letras.")



#atividade 2

def Atividade2():

#variaveis
    primeiro_valor = int(input("Qual o seu 1º valor: "))
    segundo_valor = int(input("Qual o seu 2º valor: "))
    terceiro_valor = int(input("Qual o seu 3º valor: "))

#teste logico
    if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
        print(f"O maior número desses valores é o {primeiro_valor}.")
    elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
        print(f"O maior número desses valores é o {segundo_valor}.")   
    else:
        print(f"O maior número desses valores é o {terceiro_valor}.")

#atividade 3

def Atividade3():

#variaveis
    valor_1 = int(input("Digite o 1º número: "))
    valor_2 = int(input("Digite o 2º valor: "))
    valor_3 = int(input("Digite o 3º valor: "))
 
    if valor_1 >= valor_2 >= valor_3:
        print(f"O maior número é {valor_1} e o menor número é o {valor_3}")
    elif valor_1 >= valor_3 >= valor_2:
        print(f"O maior número é {valor_1} e o menor número é o {valor_2}")
    elif valor_2 >= valor_1 >= valor_3:
        print(f"O maior número é {valor_2} e o menor número é o {valor_3}")
    elif valor_2 >= valor_2 >= valor_1:
        print(f"O maior número é {valor_2} e o menor número é o {valor_1}")
    elif valor_3 >= valor_2 >= valor_1:
        print(f"O maior número é {valor_3} e o menor número é o {valor_1}")
    elif valor_3 >= valor_1 >= valor_2:
        print(f"O maior número é {valor_3} e o menor número é o {valor_2}")
#atividade 4

def Atividade4():

#variaveis
   a = int(input("Qual o valor de A: "))
   b = int(input("Qual o valor de B: "))

#teste logico
   print(f"Os novos valores das variaveis são A={b} e B={a}")

exercicio = input("Qual exercicio você quer: ")

if exercicio == "1":
    Atividade1()
elif exercicio == "2":
    Atividade2()
elif exercicio == "3":
    Atividade3()
elif exercicio == "4":
    Atividade4()

