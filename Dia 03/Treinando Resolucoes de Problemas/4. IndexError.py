# IndexError:
    # numeros = [10, 20, 30]
    # indice = int(input("Digite um índice para acessar a lista: ")) 

    # print(numeros[indice])

# Correção do Erro:
try:
    numeros = [10, 20, 30]
    indice = int(input("Digite um índice para acessar a lista: ")) 

    print(numeros[indice])
except ValueError:
    print('Digite apenas números!')
except IndexError:
    print('Digite apenas os indices presentes na lista!')
