#Bibliotecas
import os

#Limpar tela
def limpar_tela():
    os.system('cls')
	
limpar_tela()

#Atividade 1
def Atividade1():
#Variaveis
      nota1 = float(input("Qual a 1° nota: ")) 
      nota2 = float(input("Qual a 2° nota: "))
      nota3 = float(input("Qual a 3° nota: "))
      soma = nota1 + nota2 + nota3
      media = soma / 3
#Saida      
      if media >= 7:
        print("Sua média é maior ou igual a 7 portanto você foi aprovado")
      else:
       	print("Sua média foi menor que 7 portanto você foi reprovado")
      	
#Atividade 2

def Atividade2():
#Variaveis
       temperatura = float(input("Qual temperatura você deseja converter: "))
       conversao = (temperatura * 9/5) + 32
         
       print(f"{temperatura}°C na escala Fahrenheit é igual a {conversao}°F")
       
#Atividade 3
        
def Atividade3():
#Variaveis
      numero = int(input("Qual número você deseja conferir se é positivo, negativo ou zero: "))
      
      if numero == 0:
        print(f"O número {numero} é igual a zero.")
      elif numero > 0:
        print(f"O número {numero} é positivo.")
      else:
        print(f"O número {numero} é negativo.")
        
#Atividade 4        
        
def Atividade4():
#Variaveis        
        salario = float(input("Qual seu salário atual: "))
        aumento = float(input("Qual o valor do seu aumento: "))    
        print(f"Seu novo salário é igual a R${salario+aumento:.2f}.")
        
#Atividade 5

def Atividade5():
#Variaveis
    idade = int(input("Qual sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
    
def Atividade6():
#Variaveis
    primeiro_valor = float(input("Qual o 1º valor: "))
    segundo_valor = float(input("Qual o 2º valor: "))
    terceiro_valor = float(input("Qual o 3º valor: "))

    print(f"O maior valor dentre {primeiro_valor}, {segundo_valor} e {terceiro_valor} é igual a {max(primeiro_valor, segundo_valor, terceiro_valor)}")
	
#Atividade 7

def Atividade7():
#Variaveis
    peso = float(input("Qual seu peso em Kgs: "))
    altura = float(input("Qual sua altura em Metros: "))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"Seu imc é {imc:.2f} portanto você está abaixo do peso.")
    elif imc <= 24.9:
        print(f"Seu imc é {imc:.2f} portanto você está em um peso normal.")  
    elif imc <= 29.9:
        print(f"Seu imc é {imc:.2f} portanto você está em sobrepeso.")  
    elif imc <= 39.9:
        print(f"Seu imc é {imc:.2f} portanto você está em estado de obesidade.")  
    else:
        print(f"Seu imc é {imc:.2f} portanto você está em estado de obesidade mórbida.")  

#Atividade 8

def Atividade8():
#Variaveis
    numero = int(input("Qual o 1º valor: "))
    numero2 = int(input("Qual o 1º valor: "))

    print(f"A adição é igual a {numero + numero2}\nA subtração é igual a {numero - numero2}\nA divisão é igual a {numero/numero2}\nA multiplicação é igual a {numero * numero2}")

#Atividade 9

def Atividade9():
#Variaveis
    idade = int(input("Qual a sua idade: "))

    if idade <= 2:
        print(f"Você tem {idade} anos de idade, portanto é um bebê.")
    elif idade <= 12:
        print(f"Você tem {idade} anos de idade, portanto é um criança.")
    elif idade <= 17:
        print(f"Você tem {idade} anos de idade, portanto é um adolescente.")
    elif idade <= 64:
        print(f"Você tem {idade} anos de idade, portanto é um adulto.")
    elif idade > 64:
        print(f"Você tem {idade} anos de idade, portanto é um idoso.")
    else:
        print("Coloque o valor em números")

#Atividade 10

def Atividade10():
#Variaveis
    lado1 = float(input("Qual a medida do 1º lado: "))
    lado2 = float(input("Qual a medida do 2º lado: "))
    lado3 = float(input("Qual a medida do 3º lado: "))

    if lado1 == lado2 == lado3:
        print(f"Este triângulo é um triângulo equilatero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print(f"Este triângulo é um triângulo isósceles.")
    elif lado1 < 0 or lado2 < 0 or lado3 < 0:
        print("Não é possível fazer um triângulo com estes valores.")
    else:
        print("Este triângulo é um triângulo escaleno.")

#Atividade 11

def Atividade11():
#Variaveis
    preco = float(input("Qual o preço do produto: "))
    desconto = float(input("Quantos % será descontado do produto: "))
    porcentagem = (desconto / 100) * preco

    print(f"O novo valor deste produto é igual a {preco - porcentagem}")


#Atividade 12

def Atividade12():
#Variaveis
    nome1 = input("QuaL o nome da primeira pessoa: ").capitalize()
    idade1 = int(input(f"Qual a idade de {nome1}: "))
    nome2 = input("QuaL o nome da segunda pessoa: ").capitalize()
    idade2 = int(input(f"Qual a idade de {nome2}: "))

    if idade1 > idade2:
        print(f"{nome1} é mais velho doque {nome2}.")
    else:
        print(f"{nome2} é mais velho doque {nome1}.")

#Atividade 13

def Atividade13():
#Variaveis
    valor_pago = float(input("Qual o valor pago pelo cliente: "))
    valor_do_produto = float(input("Qual o valor do produto: "))

    print(f"O troco do cliente é R${valor_pago - valor_do_produto:.2f}")


Atividade = (input("Qual atividade você deseja visualizar: "))

if Atividade == "1":
    Atividade1()
elif Atividade == "2":
    Atividade2()
elif Atividade == "3":
    Atividade3()
elif Atividade == "4":
    Atividade4()
elif Atividade == "5":
    Atividade5()
elif Atividade == "6":
    Atividade6()
elif Atividade == "7":
    Atividade7()
elif Atividade == "8":
    Atividade8()
elif Atividade == "9":
    Atividade9()
elif Atividade == "10":
    Atividade10()
elif Atividade == "11":
    Atividade11()
elif Atividade == "12":
    Atividade12()
elif Atividade == "13":
    Atividade13()