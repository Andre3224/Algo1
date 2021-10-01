# Crie um programa que lê um número do usuário, e utiliza um procedimento para 
#verificar se o número encontra-se entre 0 e 10

num = int(input('Digite um número: '))

if num > 0 and num <10: 
    print('O número está entre 0 e 10')
elif num == 0 or num == 10:
    print('O número está entre 0 e 10')
else:
    print('O número não está no intervalo.')