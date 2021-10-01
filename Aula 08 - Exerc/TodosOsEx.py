def ex1():
    print('Número dentro do intervalo')
    
    num = int(input('Digite um número: '))

    if num > 0 and num <10: 
        print('O número está entre 0 e 10')
    elif num == 0 or num == 10:
        print('O número está entre 0 e 10')
    else:
        print('O número não está no intervalo.')

def ex2():
    print('Maior e menor')
    print('-'*30)
    print('Qual o maior e qual o menor dos números?')
    num1 = float(input('Digite o número 01: '))
    num2 = float(input('Digite o número 02: '))
    num3 = float(input('Digite o número 03: '))

    if num1 > num2 and num1 > num2:
        if num2 > num3:
            print('O maior número é, ', num1)
            print('O menor número é, ', num3)
        else:
            print('O maior número é, ', num1)
            print('O menor número é, ', num2)
            
    if num2 > num1 and num1 > num2:
        if num1 > num3:
            print('O maior número é, ', num2)
            print('O menor número é, ', num3)
        else:
            print('O maior número é, ', num2)
            print('O menor número é, ', num1)
            
    if num3 > num1 and num3 > num2:
        if num2 > num1:
            print('O maior número é, ', num3)
            print('O menor número é, ', num1)
        else:
            print('O maior número é, ', num3)
            print('O menor número é, ', num2)
            
    print('-'*30)
    
def ex3():
    print('Fatorial')
    print('-'*30)
    
    num = float(input('Digite um número: '))
    fatori = 1
    while(num > 0):
        fatori = fatori * num
        num = num - 1
        
    print('O valor fatorial é de: ', fatori)
    
    print('-'*30)
    
    
def ex4():
    print('Calculadora')
    print('-'*30)
    
    x = float(input('Digite o número 1 (X): '))
    y = float(input('Digite o número 2 (y): '))

    opção = 0
    while opção != 4:
        print('''
        [1] Soma
        [2] Subtração
        [3] Divisão
        [4] Multiplicação
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
            print('erro')
            
        
        print('-'*30)




print('Resolução unica')
opção = 0
while opção != 5:
    print('''
    [1] Ex1
    [2] Ex2
    [3] Ex3
    [4] Ex4
    [5] Sair
    ''')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
        ex1()
    elif opção == 2:
        ex2()
    elif opção == 3:
        ex3()
    elif opção == 4:
        ex4()
    else:
        print('Saindo...')
        exit()