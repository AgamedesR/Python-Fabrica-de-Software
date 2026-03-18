# Erros: 

# def dividir(a, b):
#     return a / b

# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")

# resultado = dividir(int(num1), int(num2))
# print(f"Resultado: {resultado}")

# Correção dos Erros:

def dividir(a, b):
    return a / b
try:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")
except ValueError:
    print('Digite apenas números inteiros.')
except ZeroDivisionError:
    print('Erro: Divisão por Zero (0).')