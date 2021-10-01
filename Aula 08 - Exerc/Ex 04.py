#4. Faça a implementação de uma calculadora no VisuAlg. Considere que o usuário deve informar a
#operação desejada e 2 números inteiros. Implemente os procedimentos e funções para:
#- Mostrar o menu (selecionar opção);
#- Somar;
#- Subtrair;
#- Multiplicar;
#- Dividir.

x = float(input('Digite o número 1 (X): '))
y = float(input('Digite o número 2 (y): '))

opção = 0
while opção != 5:
    print('''
    [1] Soma
    [2] Subtração
    [3] Divisão
    [4] Multiplicação
    [5] Sair
    ''')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
        soma = x + y
        print('A soma é: ', soma)
    
    elif opção == 2:
        sub = x - y
        print('A subtração é: ', sub)
    elif opção == 3:
        div = x/y
        rest = x%y
        print('A divisão de X por Y é: ', div)
        print('O resto é: ', rest)
    elif opção == 4:
        mult = x*y
        print('A multiplicação (X e Y) é: ', mult)
    else:
        print('Saindo...')
        exit()