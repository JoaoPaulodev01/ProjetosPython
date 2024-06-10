def Atividade1():
    iss = 0.1
    ir = 0.2
    csll = 0.05
    faturamento = 5000
    lucro = 1000
    imposto_faturamento = iss * faturamento
    imposto_lucro = ir * lucro + csll * lucro
    imposto_total = imposto_faturamento + imposto_lucro

    print(f"O imposto a pagar é {imposto_total:.2f}")

def Atividade2():
    iphone = 1000
    ipad = 300
    airpod = 200
    macbook = 50
    applewatch = 250
    total = iphone + ipad + airpod + macbook + applewatch
    mais_vendido = max(iphone, ipad, airpod, macbook, applewatch)

    print(f"\nA quantidade de produto vendidos é de {total}\nE o produto que teve mais vendas vendeu {mais_vendido} produtos.\n")

def Atividade3():
    def cont_letra(palavra):
        vogais = "aeiou"
        return len([letra for letra in palavra.lower() if letra in vogais])
    palavra_vogal = input("Digite uma palavra para se contar as vogais: ")
    quantidade_vogais = cont_letra(palavra_vogal)
    print(f"Essa palavra tem {quantidade_vogais} vogais.")

def Atividade4():
    def contador(palavra):
        vogais = "aeiou"
        return len([letra for letra in palavra.lower() if letra in vogais])
    palavra_exemplo = "desenvolvimento"
    quantidade_vogais = palavra_exemplo(palavra_exemplo)
    print(f"A palavra '{palavra_exemplo}' tem {quantidade_vogais} vogais.")

Atividade = (input("Qual atividade você deseja visualizar: "))

if Atividade == "1":
    Atividade1()
elif Atividade == "2":
    Atividade2()
elif Atividade == "3":
    Atividade3()
elif Atividade == "4":
    Atividade4()
