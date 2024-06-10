#Atividade 1
import os

def limpar():
    os.system('cls')

def Atividade1():
    #variaveis
    distancia = float(input("Qual a distância da corrida em Kms: "))
    valor = (distancia*2.70) + 5.90
    #código
    print(f"O valor da corrida é igual R${valor:.2f}")

def Atividade2():
    #variaveis
    velocidade = int(input("Qual velocidade o carro estava: "))
    multa = 50 + (velocidade - 100) * 8
    #código
    if velocidade > 100:
        print(f"Você foi multado em R${multa:.2f}")
    else:
        print("Você não foi multado")

def Atividade3():
    ano = int(input("Qual ano você deseja saber se é bissexto ou não: "))
    bissexto = ano % 4 and ano % 400

    if bissexto == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")

def Atividade4():
    #variaveis
    salario = float(input("Qual o seu salário: "))
    salario15 = salario * 0.15 + salario
    salario30 = salario * 0.30 + salario

    if salario > 1420:
        print(f"Seu salário com o aumento será de R${salario15:.2f}.")
    else:
        print(f"Seu salário com o aumento será de R${salario30:.2f}.")

Atividade = (input("Qual atividade você deseja visualizar: "))

if Atividade == "1":
    Atividade1()
elif Atividade == "2":
    Atividade2()
elif Atividade == "3":
    Atividade3()
elif Atividade == "4":
    Atividade4()

