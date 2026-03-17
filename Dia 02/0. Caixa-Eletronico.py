import os

def inicio():
    print('''
          *****************************
          SIMULADOR DE CAIXA ELETRÔNICO
          *****************************
          ''')
    print(f'Valor total da conta: R${saldo}\n')

    print ('1. Deposito')
    print ('2. Saque')
    print('3. Extrato')
    print('4. Sair\n')

saldo = 0
transacoes = []

while True:
    inicio()
    opcao_escolhida = int(input('Escolha a oção desejado: '))

    if opcao_escolhida == 1:
        deposito = int(input('\nDigite o valor do deposito: '))
        saldo = saldo + deposito
        transacoes.append(f'Desposito: R${deposito}')
        print(f'Valor total da conta: R${saldo}')

    elif opcao_escolhida == 2:
        saque = int(input('\nDigite o valor do saque: '))
        if saque > saldo:
            print('Saldo insuficiente!\n')
            saldo = saldo - saque
            print(f'Valor total da conta: R${saldo}')
        else:
            saldo= saldo - saque
            transacoes.append(f'Saque: R${saque}')
            print(f'Valor total da conta: R${saldo}')

    elif opcao_escolhida == 3:
        os.system('cls')
        print('''
            ***********************
                    EXTRATO
            ***********************
            ''')
        if len(transacoes) == 0:
            print('Sem histórico de transações.\n')
        else:
            for t in transacoes:
                print(t)
            print(f'\nSaldo atual: {saldo}\n')  

    else:
        os.system('cls')
        print('\nSaindo do programa...\n')
        break