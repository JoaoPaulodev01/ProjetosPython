from tkinter import *
import math

def delete():
    display.delete(0, END)

def get_input():
    try:
        return float(display.get())
    except ValueError:
        display.delete(0, END)
        display.insert(0, "Erro")
        return None

def operation(op):
    global operator
    global first_number
    first_number = get_input()
    if first_number is not None:
        operator = op
        display.delete(0, END)

def calculate():
    global step
    if step == 2:
        global b
        b = get_input()
        if b is not None:
            step = 3
            display.delete(0, END)
  
    elif step == 3:
        global c
        c = get_input()
        if c is not None:
            delta_value = b**2 - 4*a*c
            display.delete(0, END)
            display.insert(0, f"Δ = {round(delta_value, 3)}, ")

            if delta_value < 0:
                display.insert(END, " (sem raízes reais)")
            elif delta_value == 0:
                x = -b / (2 * a)
                display.insert(END, f" x = {round(x, 3)}")
            else:
                x1 = (-b + math.sqrt(delta_value)) / (2 * a)
                x2 = (-b - math.sqrt(delta_value)) / (2 * a)
                display.insert(END, f" x1 = {round(x1, 3)}, x2 = {round(x2, 3)}")
            step = 1  # Reset step after calculation
    else:
        second_number = get_input()
        if second_number is not None and operator and first_number is not None:
            if operator == '+':
                result = first_number + second_number
            elif operator == '-':
                result = first_number - second_number
            elif operator == '*':
                result = first_number * second_number
            elif operator == '/':
                if second_number == 0:
                    display.delete(0, END)
                    display.insert(0, "Erro")
                    return
                result = first_number / second_number
            display_result(result)

def mais():
    operation('+')

def menos():
    operation('-')

def multiplicacao():
    operation('*')

def divisao():
    operation('/')

def raiz():
    n1 = get_input()
    if n1 is not None:
        if n1 < 0:
            display.delete(0, END)
            display.insert(0, "Erro")
        else:
            result = math.sqrt(n1)
            display_result(result)

def delta():
    global step
    global a
    a = get_input()
    if a is not None:
        step = 2
        display.delete(0, END)

def fatorial():
    numero = get_input()
    if numero is not None:
        if numero < 0:
            display.delete(0, END)
            display.insert(0, "Erro")
        else:
            result = math.factorial(int(numero))
            display_result(result)

def display_result(result):
    display.delete(0, END)
    display.insert(0, str(round(result, 3)))

def insert_minus():
    current_text = display.get()
    if '-' not in current_text:
        display.insert(END, '-')

janela = Tk()
janela.title("Calculadora")
janela.configure(bg='black')  # Definindo o fundo preto para a janela

# Tamanho da janela para encaixar no modo retrato de um telefone
largura = janela.winfo_screenwidth() // 2
altura = janela.winfo_screenheight() // 1.5
janela.geometry(f"{largura:.0f}x{altura:.0f}")

# Campo de exibição
display = Entry(janela, width=30, font=('Helvetica', 10), borderwidth=5, bg='black', fg='white')
display.pack(padx=10, pady=20)

# Frame para os botões
bottom_frame = Frame(janela, bg='black')
bottom_frame.pack(side='bottom', fill='x', pady=10)

# Altura dos botões
button_height = 3

# Botões na parte inferior
Button(bottom_frame, text="C", font=('Helvetica', 14), width=4, height=button_height, command=delete, bg='black', fg='orange').grid(row=0, column=0)
Button(bottom_frame, text="!", font=('Helvetica', 14), width=4, height=button_height, command=fatorial, bg='black', fg='orange').grid(row=0, column=1)
Button(bottom_frame, text="∆", font=('Helvetica', 14), width=4, height=button_height, command=delta, bg='black', fg='orange').grid(row=0, column=2)
Button(bottom_frame, text="+", font=('Helvetica', 14), width=4, height=button_height, command=mais, bg='black', fg='orange').grid(row=0, column=3)
Button(bottom_frame, text="7", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '7'), bg='black', fg='white').grid(row=1, column=0)
Button(bottom_frame, text="8", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '8'), bg='black', fg='white').grid(row=1, column=1)
Button(bottom_frame, text="9", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '9'), bg='black', fg='white').grid(row=1, column=2)
Button(bottom_frame, text="-", font=('Helvetica', 14), width=4, height=button_height, command=menos, bg='black', fg='orange').grid(row=1, column=3)
Button(bottom_frame, text="4", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '4'), bg='black', fg='white').grid(row=2, column=0)
Button(bottom_frame, text="5", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '5'), bg='black', fg='white').grid(row=2, column=1)
Button(bottom_frame, text="6", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '6'), bg='black', fg='white').grid(row=2, column=2)
Button(bottom_frame, text="×", font=('Helvetica', 14), width=4, height=button_height, command=multiplicacao, bg='black', fg='orange').grid(row=2, column=3)
Button(bottom_frame, text="1", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '1'), bg='black', fg='white').grid(row=3, column=0)
Button(bottom_frame, text="2", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '2'), bg='black', fg='white').grid(row=3, column=1)
Button(bottom_frame, text="3", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '3'), bg='black', fg='white').grid(row=3, column=2)
Button(bottom_frame, text="÷", font=('Helvetica', 14), width=4, height=button_height, command=divisao, bg='black', fg='orange').grid(row=3, column=3)
Button(bottom_frame, text="0", font=('Helvetica', 14), width=4, height=button_height, command=lambda: display.insert(END, '0'), bg='black', fg='white').grid(row=4, column=1)
Button(bottom_frame, text="√", font=('Helvetica', 14), width=4, height=button_height, command=raiz, bg='black', fg='white').grid(row=4, column=0)
Button(bottom_frame, text="-", font=('Helvetica', 14), width=4, height=button_height, command=insert_minus, bg='black', fg='white').grid(row=4, column=2)
Button(bottom_frame, text="=", font=('Helvetica', 14), width=4, height=button_height, command=calculate, bg='black', fg='orange').grid(row=4, column=3, columnspan=4)

janela.mainloop()
