def inicio():
    print('''
        **************************
            CALCULADORA EM POO
        **************************
    ''')

def exibir_opcoes():
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Exibir Histórico')
    print('0 - Sair')

class Calculadora:
    def __init__(self):
        self.historico = []

    def soma(self, a, b):
        resultado = a + b
        self.historico.append(f'Soma:          {a} + {b} = {resultado}')
        return resultado
    
    def subtracao(self, a, b):
        resultado = a - b
        self.historico.append(f'Subtração: {a} - {b} = {resultado}')
        return resultado
    
    def multiplicacao(self, a, b):
        resultado = a * b
        self.historico.append(f'Multiplicação: {a} x {b} = {resultado}')
        return resultado
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError('Divisão por Zero.')
        resultado = a / b
        self.historico.append(f'Divisão: {a} / {b} = {resultado}')
        return resultado

    def exibir_historico(self):
        if not self.historico:
            print('\nNenhuma operação realizada.\n')
        else:
            print('''
                ****************
                    HISTÓRICO
                ****************
                ''')
            for i, operacao in enumerate(self.historico, 1):
                print(f'  {i}. {operacao}')

def selecionar_opcao(calc):
    while True:
        try:
            exibir_opcoes()
            opcao = int(input('\nEscolha uma opção: '))

            if opcao == 0:
                print('\nEncerrando...')
                break

            elif opcao in [1, 2, 3, 4]:
                a = int(input('Digite o primeiro número: '))
                b = int(input('Digite o segundo número: '))

                if opcao == 1:
                    print('\nResultado:', calc.soma(a, b))
                    print()
                elif opcao == 2:
                    print('\nResultado:', calc.subtracao(a, b))
                    print()
                elif opcao == 3:
                    print('\nResultado:', calc.multiplicacao(a, b))
                    print()
                elif opcao == 4:
                    print('\nResultado:', calc.divisao(a, b))
                    print()

            elif opcao == 5:
                calc.exibir_historico()

            else:
                print('\nOpção inválida!')

        except ValueError as erro:
            print(f'\nErro: {erro}')

def main():
    inicio()
    calc = Calculadora()
    selecionar_opcao(calc)

if __name__ == '__main__':
    main()