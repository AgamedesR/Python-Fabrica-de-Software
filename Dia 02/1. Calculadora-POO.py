import os

# CLASSE
class Calculadora:
    def adicao(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        return a / b
    
# PRINCIPAL
calc = Calculadora()
historico = []

def nome_do_programa():
    exibir_subtitulo('Calculadora em POO')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
  
def opcao_invalida(texto):
    print(texto)
    voltar_ao_menu_principal()

def exibir_opcoes():
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Exibir Histórico')
    print('6 - Sair')

def digite_os_numeros():
    a = float(input('\nDigite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    return a, b 

def escolher_opcoes():
    opcao_escolhida = int(input('\nDigite a opção desejada: ')) 

    try:
        if opcao_escolhida == 1:
            exibir_subtitulo('Operação de Adição')
            a, b = digite_os_numeros()
            print(f'\n{a} + {b} = {calc.adicao(a, b)}\n')
            historico.append(f'{a} + {b} = {calc.adicao(a, b)}')
            voltar_ao_menu_principal()

        elif opcao_escolhida == 2:
            exibir_subtitulo('Operação de Subtração')
            a, b = digite_os_numeros()
            print(f'{a} - {b} = {calc.subtracao(a, b)}\n')
            historico.append(f'{a} - {b} = {calc.subtracao(a, b)}')
            voltar_ao_menu_principal()

        elif opcao_escolhida == 3:
            exibir_subtitulo('Operação de Multiplicação')
            a, b = digite_os_numeros()
            print(f'\n{a} x {b} = {calc.multiplicacao(a, b)}\n')
            historico.append(f'{a} x {b} = {calc.multiplicacao(a, b)}')
            voltar_ao_menu_principal()

        elif opcao_escolhida == 4:
            exibir_subtitulo('Operação de Divisão')
            a, b = digite_os_numeros()
            print(f'\n{a} ÷ {b} = {calc.divisao(a, b)}\n')
            historico.append(f'{a} ÷ {b} = {calc.divisao(a, b)}')
            voltar_ao_menu_principal()

        elif opcao_escolhida == 5:
            exibir_subtitulo('Histórico')
            if not historico:
                print('Nenhuma operação realizada ainda.')
            else:
                for i, operacao in enumerate(historico, start=1):
                    print(f'{i}. {operacao}')   
            voltar_ao_menu_principal()
              
        elif opcao_escolhida == 6:
            os.system('cls')
            print('\nEncerrando Calculadora...\n')
            
        else:
            opcao_invalida('Erro! Digite um número de 1 a 6.')

    except ValueError:
        opcao_invalida('Erro! Digite o número inteiro.')
    

def main():
    '''
    Organiza o código principal em uma função.
    '''
    os.system('cls')
    nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    '''
    Garante que o programa só roda se executar este arquivo diretamente.
    '''
    main()
