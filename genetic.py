def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b

def calculadora():
    print("Bem vindo à sua calculadora: ")
    print("Escolha alguma operação matemática disponível: ")
    print("Aperte 1 para adição")
    print("Aperte 2 para subtração")
    print("Aperte 3 para multiplicação")
    print("Aperte 4 para divisão")

calculadora()

escolha = input('Escolha a sua operação: ')

num1 = float(input('Digite o seu primeiro número: '))
num2 = float(input('Digite o seu segundo número: '))

if escolha == '1':
    print(f"{num1} + {num2} = {addition(num1, num2)}")
elif escolha == '2':
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
elif escolha == '3':
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
elif escolha == '4':
    print(f"{num1} / {num2} = {division(num1, num2)}")
else:
    print('Opção inválida')